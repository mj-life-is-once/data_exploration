import os
import sys

from pydata.dash.app import DashReport
from pydata.dash.jupyter import run_notebook


def main(args=None) -> None:
    """_summary_
    Main entry point for the CLI
    """
    if not args:
        args = sys.argv[1:]

    if args and args[0] == "dash":
        print("Running Dash App")
        dash = DashReport()
        dash.app.run_server(debug=True)

    if args and args[0] == "report":
        read_name = args[1] if len(args) > 1 else "UserReport.ipynb"
        cwd = os.getcwd()
        if read_name == "UserReport.ipynb":
            userId = args[2] if len(args) > 2 else "35897499"
            run_notebook(
                os.path.join(os.getcwd(), f"data/exploration/{read_name}"),
                output_path=os.path.join(
                    cwd, "data/exploration/report", f"Generated_report_{userId}.html"
                ),
                userId=userId,
            )
        elif read_name == "AllReport.ipynb":
            run_notebook(
                os.path.join(os.getcwd(), f"data/exploration/{read_name}"),
                output_path=os.path.join(
                    cwd, "data/exploration/report", "Generated_report.html"
                ),
            )
