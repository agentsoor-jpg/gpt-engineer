from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import os
import subprocess
import uuid
import html

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
      <head>
        <title>GPT Engineer UI</title>
      </head>
      <body style="font-family: Arial; max-width: 800px; margin: 40px auto;">
        <h1>GPT Engineer UI</h1>

        /generate
          <textarea 
            name="prompt" 
            rows="10" 
            style="width:100%;" 
            placeholder="Describe the app you want..."
          ></textarea>

          <br><br>

          <button type="submit">
            Generate
          </button>
        </form>
      </body>
    </html>
    """

@app.post("/generate", response_class=HTMLResponse)
def generate(prompt: str = Form(...)):
    project_id = str(uuid.uuid4())[:8]
    project_dir = f"/app/projects/project-{project_id}"
    os.makedirs(project_dir, exist_ok=True)

    prompt_file = os.path.join(project_dir, "prompt")

    with open(prompt_file, "w", encoding="utf-8") as f:
        f.write(prompt)

    try:
        result = subprocess.run(
            ["gpt-engineer", project_dir],
            capture_output=True,
            text=True,
            timeout=300
        )

        output = result.stdout + "\n" + result.stderr

    except Exception as e:
        output = str(e)

    safe_output = html.escape(output)

    return f"""
    <html>
      <head>
        <title>GPT Engineer Result</title>
      </head>
      <body style="font-family: Arial; max-width: 900px; margin: 40px auto;">
        <h2>Result</h2>

        <pre style="white-space: pre-wrap; background:#f4f4f4; padding:20px;">
{safe_output}
        </pre>

        <br>

        /Back</a>
      </body>
    </html>
    """
