from flask import Flask, render_template, request, redirect
import pandas as pd
import os


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/scouting")
def scouting():
    return render_template("scouting.html")


@app.route("/scouts")
def scouts():
    html = pd.read_excel("scouting_data.xlsx", sheet_name="Sheet1").to_html()
    return render_template("scouts.html", html_code=html)


@app.route("/auth", methods=["POST"])
def auth():
    passwd = request.form.get("pass")
    if passwd == "tutumlu":
        return redirect("/scouting")
    else:
        return render_template("fuck.html")


@app.route("/excel", methods=["POST"])
def excelPost():
    teamnumber = request.form.get("team-number")
    scoutname = request.form.get("scout-name")
    location = request.form.get("location")

    centerpl = request.form.get("center-lp")
    if centerpl == "1":
        centerpl = 1
    else:
        centerpl = 0

    leavesz = request.form.get("leave-sz")
    if leavesz == "1":
        leavesz = 1
    else:
        leavesz = 0

    speakerScoredAuto = request.form.get("speakerScoredAuto")
    speakerMissedAuto = request.form.get("speakerMissedAuto")
    ampScoredAuto = request.form.get("ampScoredAuto")
    ampMissedAuto = request.form.get("ampMissedAuto")

    speakerScoredTele = request.form.get("speakerScoredTele")
    speakerMissedTele = request.form.get("speakerMissedTele")
    ampScoredTele = request.form.get("ampScoredTele")
    ampMissedTele = request.form.get("ampMissedTele")
    amplifiedScoredTele = request.form.get("amplifiedScoredTele")
    trapScoredTele = request.form.get("TrapScoredTele")
    trapMissedTele = request.form.get("TrapMissedTele")

    park = request.form.get("park")

    spotlit = request.form.get("spotlit")
    if spotlit == "1":
        spotlit = "true"
    else:
        spotlit = "false"

    pickUp = request.form.get("pickUp")
    if pickUp == "1":
        pickUp = "true"
    else:
        pickUp = "false"

    defense = request.form.get("defense")
    driver = request.form.get("driver")
    intake = request.form.get("intake")
    speed = request.form.get("speed")
    stability = request.form.get("stability")

    drivetrain = request.form.get("drivetrain")

    note = request.form.get("note")

    print(teamnumber)

    data = {
        "Location": [location],
        "Team": [teamnumber],
        "Name": [scoutname],
        "CenterPickUp": [centerpl],
        "LeaveCommunity": [leavesz],
        "Speaker Scored Auto": [speakerScoredAuto],
        "Speaker Missed Auto": [speakerMissedAuto],
        "Amp Scored Auto": [ampScoredAuto],
        "Amp Missed Auto": [ampMissedAuto],
        "Speaker Scored Tele": [speakerScoredTele],
        "Speaker Missed Tele": [speakerMissedTele],
        "Amp Scored Tele": [ampScoredTele],
        "Amp Missed Tele": [ampMissedTele],
        "Amplified Scored Tele": [amplifiedScoredTele],
        "Trap Scored Tele": [trapScoredTele],
        "Trap Missed Tele": [trapMissedTele],
        "Park": [park],
        "Spotlit": [spotlit],
        "Pick Up": [pickUp],
        "Defense": [defense],
        "Driver": [driver],
        "Intake": [intake],
        "Speed": [speed],
        "Stability": [stability],
        "Drivetrain": [drivetrain],
        "Notes": [note],
    }

    df = pd.DataFrame(data)
    existing_df = pd.read_excel("scouting_data.xlsx")

    combined_df = pd.concat([existing_df, df], ignore_index=True)

    combined_df.to_excel("scouting_data.xlsx", index=False)

    combined_df_csv = combined_df.to_csv

    # Save the DataFrame to an Excel file

    return redirect("/scouting")

@app.route("/delrow",methods=["POST"])
def delRov():
    row = int(request.form.get("row"))
    
    passwd = request.form.get("passwd")

    exsinting_df = pd.read_excel("scouting_data.xlsx")

    if passwd == "sebnem":
        updated_df = exsinting_df.drop(index=row)
        updated_df.to_excel("scouting_data.xlsx", index=False)



    return redirect("/scouts")




def excel_sheet_Func():
    existing_df=pd.read_excel("scouting_data.xlsx")
    
    return


app.run(debug=True, host="0.0.0.0", port=80)
