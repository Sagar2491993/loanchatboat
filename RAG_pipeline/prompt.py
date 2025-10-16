import os

def load_prompt_templates():
    try:
        base_dir = r"D:\Sagar\bank of maharashtra loans gen ai project\prompt"
        file_paths = {
            "main_template": os.path.join(base_dir, "main_template.txt"),
            "schema_description": os.path.join(base_dir, "doc_description.txt"),
        }

        prompt_data = {}

        # Load both prompt files
        for key, path in file_paths.items():
            if not os.path.exists(path):
                raise FileNotFoundError(f" Missing file: {path}")
            with open(path, "r", encoding="utf-8") as f:
                prompt_data[key] = f.read().strip()

        formatted_prompt = prompt_data["main_template"].format(
            doc_description=prompt_data["schema_description"],
            context="{context}",
            question="{question}"
        )

        return formatted_prompt

    except Exception as e:
        print(f"Error loading prompt templates: {e}")
        raise
