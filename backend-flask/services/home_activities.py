from datetime import datetime, timedelta, timezone
from opentelemetry import trace
import logging

from lib.db import db

#for aws xray
#tracer = trace.get_tracer("home.activities")

class HomeActivities:
  def run(cognito_user_id=None):
    #for clodwatch logs
    #logger.info("HomeActivities")
    #this is awsXray
    #with tracer.start_as_current_span("avctivities-home-test-span"):
    #  span = trace.get_current_span()
    #  now = datetime.now(timezone.utc).astimezone()
    #  span.set_attribute("app.now", now.isoformat)
    sql = db.template('activities','home')
    results = db.query_array_json(sql)

    #is for honeycomb
    #span.set_attribute("app.result_lenght", len(results))
    return results