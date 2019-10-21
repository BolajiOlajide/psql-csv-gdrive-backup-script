\copy (SELECT app_mealservice.date, app_mealservice.date_modified, app_mealservice.user_id, app_slackuser.id, app_slackuser.firstname, app_slackuser.lastname, app_slackuser.user_type, app_mealservice.breakfast, app_mealservice.lunch FROM app_mealservice LEFT JOIN app_slackuser ON app_mealservice.user_id=app_slackuser.id WHERE date < CURRENT_TIMESTAMP ORDER BY app_mealservice.date DESC) to '/app/backup.csv' with DELIMITER ',' csv header;

-- DELETE FROM app_mealservice WHERE date < CURRENT_TIMESTAMP;