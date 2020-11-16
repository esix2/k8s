from flask import Flask

app = Flask("server1")



@app.route("/<string:idx>")
def return_value(idx):
    if len(idx) == 1:
      return getRole("")
    else:
      return getRole(idx)

def getRole(person):
  if person=="ez":
    return {"name": "Ehsan Zandi", "role" : "the applicant for R&D job position"}
  elif person=="jj":
    return {"name": "Jeniffer Juchens", "role" : "Head of Human Resources"}
  elif person=="je":
    return {"name": "Justin Eichenlaub", "role" : "Head of Cellular Solution"}
  return {"name": 0, "role" : 0}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=2000,debug=True)
