from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Data model for a report
class Report(BaseModel):
    reporter_name: str
    description: str
    platform: str

# Store reports in memory
reports: List[Report] = []

# Endpoint to submit a report
@app.post("/report")
def submit_report(report: Report):
    reports.append(report)
    return {"message": "Report submitted successfully", "report": report}

@app.post("/reports/bulk")
def submit_multiple_reports(new_reports: List[Report]):
    if not new_reports:
        raise HTTPException(status_code=400, detail="No reports provided")
    reports.extend(new_reports)
    return {"message": f"{len(new_reports)} reports submitted", "reports": new_reports}


# Endpoint to view all reports
@app.get("/reports")
def get_reports():
    return {"total_reports": len(reports), "reports": reports}

# NEW: Endpoint to delete a report by ID
@app.delete("/report/{report_id}")
def delete_report(report_id: int):
    if report_id < 0 or report_id >= len(reports):
        return {"error": "Invalid report ID"}
    deleted = reports.pop(report_id)
    return {"message": "Report deleted", "report": deleted}

# NEW: Endpoint to filter reports by platform
@app.get("/reports/filter")
def filter_reports(platform: str):
    filtered = [r for r in reports if r.platform.lower() == platform.lower()]
    return {"platform": platform, "count": len(filtered), "reports": filtered}