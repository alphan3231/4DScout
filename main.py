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
    return render_template("scouts.html")

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
    
    centerpl = request.form.get("center-lp")
    leavesz = request.form.get("leave-sz")


    speakerScoredAuto = request.form.get("speakerScoredAuto")
    speakerMissedAuto = request.form.get("speakerMissedAuto")
    ampScoredAuto = request.form.get("ampScoredAuto")
    ampMissedAuto = request.form.get("ampMissedAuto")

    speakerScoredTele = request.form.get("speakerScoredTele")
    speakerMissedTele = request.form.get("speakerMissedTele")
    ampScoredTele = request.form.get("ampScoredTele")
    ampMissedTele = request.form.get("ampMissedTele")
    amplifiedScoredTele = request.form.get("amplifiedScoredTele")
    trapScoredTele = request.form.get("trapScoredTele")
    trapMissedTele = request.form.get("trapMissedTele"),
    
    park = request.form.get("park")
    spotlit = request.form.get("spotlit")
    pickUp = request.form.get("pickUp")

    defense = request.form.get("defense")
    driver = request.form.get("driver")
    intake = request.form.get("intake")
    speed = request.form.get("speed")
    stability = request.form.get("stability")

    drivetrain = request.form.get("drivetrain")

    note = request.form.get("note")

    print(teamnumber)
    

    data = {
        "Team": [teamnumber],
        "Name": [scoutname],
        "CLP": [centerpl],
        "LSZ": [leavesz],
        "SSA": [speakerScoredAuto],
        "SMA": [speakerMissedAuto],
        "ASA": [ampScoredAuto],
        "AMA": [ampMissedAuto],
        "SST": [speakerScoredTele],
        "SMT": [speakerMissedTele],
        "AST": [ampScoredTele],
        "AMT": [ampMissedTele],
        "AlifiedST": [amplifiedScoredTele],
        "TST": [trapScoredTele],
        "TMT": [trapMissedTele],
        "Park": [park],
        "Spotlit": [spotlit],
        "PickUp": [pickUp],
        "Defense": [defense],
        "Driver": [driver],
        "Intake": [intake],
        "Speed": [speed],
        "Stability": [stability],
        "Drivetrain": [drivetrain],
        "Notes" : [note]
    }

    # data = {
    #     "Team Number": [teamnumber],
    #     "Scout Name": [scoutname],
    #     "Center LP": [centerpl],
    #     "Leave SZ": [leavesz],
    #     "Speaker Scored Auto": [speakerScoredAuto],
    #     "Speaker Missed Auto": [speakerMissedAuto],
    #     "Amp Scored Auto": [ampScoredAuto],
    #     "Amp Missed Auto": [ampMissedAuto],
    #     "Speaker Scored Tele": [speakerScoredTele],
    #     "Speaker Missed Tele": [speakerMissedTele],
    #     "Amp Scored Tele": [ampScoredTele],
    #     "Amp Missed Tele": [ampMissedTele],
    #     "Amplified Scored Tele": [amplifiedScoredTele],
    #     "Trap Scored Tele": [trapScoredTele],
    #     "Trap Missed Tele": [trapMissedTele],
    #     "Park": [park],
    #     "Spotlit": [spotlit],
    #     "Pick Up": [pickUp],
    #     "Defense": [defense],
    #     "Driver": [driver],
    #     "Intake": [intake],
    #     "Speed": [speed],
    #     "Stability": [stability],
    #     "Drivetrain": [drivetrain]
    # }

    df = pd.DataFrame(data)

    # Save the DataFrame to an Excel file
    df.to_excel("scouting_data.xlsx", index=False)

    return redirect("/scouting")

app.run(debug=True)