from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)

MY_EMAIL = "yusufceri581@gmail.com"
MY_PASSWORD = "ftkduhqjyfezhngj"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/work")
def work():
      return render_template("work.html")

@app.route("/contact", methods=["POST","GET"])
def contact():
        if request.method == "POST":
            data = request.form
            print(data["name"])
            print(data["email"])
            print(data["phone"])
            print(data["message"])
            contents = f"Name: {data['name']} \n" \
                    f"Email: {data['email']} \n" \
                    f"Phone: {data['phone']} \n" \
                    f"Message: {data['message']} \n"
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs="yusicheri15@gmail.com",
                    msg=f"Subject: New Message!\n\n"
                        f"{contents}"
                )
            return render_template("contact.html", msg_sent=True)
        return render_template("contact.html", msg_sent=False)

if __name__ == "__main__":
    app.run(debug=True)

