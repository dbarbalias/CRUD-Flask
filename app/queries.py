same_day = "SELECT id FROM task WHERE date(timestamp)=date('now');"
roll_over = "SELECT id FROM task WHERE status=0 AND date(timestamp) != date('now');"
