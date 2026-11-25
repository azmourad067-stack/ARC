def load_raw(engine: Engine, until: date | None = None) -> dict[str, pd.DataFrame]:
    until = until or date(2100, 1, 1)

    races = _read(engine, """
        SELECT r.race_id, r.race_date, r.reunion_num, r.course_num, r.discipline,
               r.distance_m, r.prize_eur, r.declared_runners, r.scheduled_start_utc,
               r.first_observed_at, r.result_final, r.country, rc.code AS racecourse,
               CASE WHEN LOWER(r.conditions_text) LIKE '%autostart%' THEN 1 ELSE 0 END
                   AS autostart
        FROM races r
        LEFT JOIN racecourses rc ON rc.racecourse_id = r.racecourse_id
        WHERE r.race_date <= :until
    """, until=until)

    entries = _read(engine, """
        SELECT e.*
        FROM race_entries e
        JOIN races r ON r.race_id = e.race_id
        WHERE r.race_date <= :until
    """, until=until)

    results = _read(engine, """
        SELECT res.race_id, res.num_pmu, res.finish_position, res.incident,
               res.reduction_km_s
        FROM race_results res
        JOIN races r ON r.race_id = res.race_id
        WHERE r.race_date <= :until
    """, until=until)

    horses = _read(engine, """
        SELECT horse_id, sire, dam_sire
        FROM horses
    """)

    going = _read(engine, """
        SELECT c.race_id, c.going_label, c.penetrometer, c.observed_at
        FROM racecourse_conditions c
        JOIN races r ON r.race_id = c.race_id
        WHERE r.race_date <= :until
    """, until=until)

    odds = _read(engine, """
        SELECT o.race_id, o.num_pmu, o.pool, o.odds,
               o.published_at, o.observed_at
        FROM odds_snapshots o
        JOIN races r ON r.race_id = o.race_id
        WHERE r.race_date <= :until
          AND o.odds_kind = 'reference'
          AND o.bet_type = 'SIMPLE_GAGNANT'
    """, until=until)

    numeric_columns = (
        (
            races,
            ["distance_m", "prize_eur", "declared_runners"],
        ),
        (
            entries,
            [
                "age",
                "draw",
                "weight_kg",
                "weight_carried_kg",
                "handicap_distance_m",
                "handicap_value",
                "career_starts",
                "career_wins",
                "career_places",
                "career_earnings",
            ],
        ),
        (
            results,
            ["finish_position", "reduction_km_s"],
        ),
        (
            odds,
            ["odds"],
        ),
    )

    for frame, columns in numeric_columns:
        for column in columns:
            frame[column] = pd.to_numeric(
                frame[column],
                errors="coerce",
            ).astype("float64")

    races["race_date"] = pd.to_datetime(
        races["race_date"]
    ).dt.date

    races["scheduled_start_utc"] = _utc(
        races["scheduled_start_utc"]
    )

    races["first_observed_at"] = _utc(
        races["first_observed_at"]
    )

    entries["observed_at"] = _utc(
        entries["observed_at"]
    )

    odds["published_at"] = _utc(
        odds["published_at"]
    )

    odds["observed_at"] = _utc(
        odds["observed_at"]
    )

    going["observed_at"] = _utc(
        going["observed_at"]
    )

    return {
        "races": races,
        "entries": entries,
        "results": results,
        "odds": odds,
        "going": going,
        "horses": horses,
    }
