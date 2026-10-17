import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 待辦清單資料庫（包含 task_name, priority, details 三個欄位）
tasks = [
    {
        "task_name": "完成課堂報告",
        "priority": "高",
        "details": "整理專案簡報與文獻，下週三前繳交。"
    },
    {
        "task_name": "複習考試科目",
        "priority": "中",
        "details": "練習重點章節題庫並整理錯題筆記。"
    }
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task_name = request.form.get("task_name")
        priority = request.form.get("priority")
        details = request.form.get("details")

        if task_name and priority and details:
            tasks.insert(0, {
                "task_name": task_name,
                "priority": priority,
                "details": details
            })
        return redirect(url_for("index"))

    return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)