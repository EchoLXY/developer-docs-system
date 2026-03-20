import json

def generate_markdown(api_data):
    md = f"# {api_data['name']}\n\n"
    md += f"## Endpoint\n{api_data['method']} {api_data['path']}\n\n"
    md += "## Description\n"
    md += f"{api_data['description']}\n\n"

    md += "## Request Body\n```json\n"
    md += json.dumps(api_data["request"], indent=2)
    md += "\n```\n\n"

    md += "## Response\n```json\n"
    md += json.dumps(api_data["response"], indent=2)
    md += "\n```\n"

    return md

if __name__ == "__main__":
    with open("sample_input.json") as f:
        data = json.load(f)

    output = generate_markdown(data)

    with open("../api/generated-create-order.md", "w") as f:
        f.write(output)

    print("Documentation generated successfully.")
