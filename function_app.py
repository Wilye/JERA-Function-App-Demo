import datetime
import logging
import azure.functions as func
from JERA_main import JERA_main
import pytz

app = func.FunctionApp()

@app.schedule(schedule="0 0 8 * * 5", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def TimerTrigger(myTimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    JERA_main()