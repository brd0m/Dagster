from typing import List
from dagster import asset, AssetExecutionContext, define_asset_job, AssetSelection, Definitions, ScheduleDefinition

@asset
def extract_loc1(context: AssetExecutionContext):
    """
    Getting data from location A. 
    """
    #docstring ^
    data = [1,2,3]
    context.log.info(f"Obtained data from location A: {data}")
    return data

@asset()
def extract_loc2(context: AssetExecutionContext):
    """
    Getting data from location B.
    """
    data = [4,5,6]
    context.log.info(f"Obtained data from location B: {data}")
    return data

@asset()
def merge_transform(context: AssetExecutionContext, extract_loc1: List, extract_loc2: List):
    """
    Transforming data from both locations
    """
    appended_data = (extract_loc1 + extract_loc2)*2
    context.log.info(f"Data has been merged and transformed!: {appended_data}")
    return appended_data

@asset()
def visualize(context: AssetExecutionContext, merge_transform: List):
    """
    Lets load it into our visualization tool!
    """
    context.log.info("Done!")
    return "Pretend this is a graph"

defs = Definitions(
    assets=[extract_loc1, extract_loc2, merge_transform, visualize],
    jobs=[
        define_asset_job(
            name="monthly_consolidation",
            selection=AssetSelection.all(),
        )
    ],
    schedules=[
        ScheduleDefinition(
            name="annyeong_scheduler",
            job_name="monthly_consolidation",
            cron_schedule="0 0 30 1-12 *", #https://crontab.guru
        )
    ],
)