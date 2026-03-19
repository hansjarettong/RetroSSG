import yaml
import os
from typing import Dict


# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)

# Load YAML content into site_template
yaml_path = os.path.join(script_dir, "site-template.yaml")
with open(yaml_path, "r") as yaml_file:
    site_template = yaml.safe_load(yaml_file)


def dict_to_html_list(input_dict: Dict[str, list]) -> str:
    output = ["<ul>"]
    for k, v in input_dict.items():
        output.append(f"\t<li>{k} \\")
        output.append("\t<ul>")
        for i in v:
            output.append(f"\t\t\t<li>{i}</li>")
        output.append("\t</ul>")
        output.append("\t</li>")
    output.append("</ul>")

    return "\n".join(output)


def render_html(
    site_template: dict,
    output_dir: str = "build",
    var_name: str = None,
    parent_template: str = None,
):
    # fill in variables and append to pages list
    for page, content in site_template.items():
        # create folder if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        template_path = os.path.join(script_dir, content["template"])
        with open(template_path, "r") as f:
            template = f.read()

        # inherit from parent template
        if var_name and parent_template:
            template = parent_template.replace(f"{{{{{var_name}}}}}", template)

        # fill in the variables
        for var, val in content["variables"].items():
            # TODO: implement if statement to handle md
            if isinstance(val, dict):
                # skip templates, handle them in the end
                if "template" in list(val.values())[0]:
                    continue
                # if dict is not a template, handle as list
                val = dict_to_html_list(val)

            if val.endswith(".html"):
                with open(os.path.join(script_dir, val), "r") as f:
                    val = f.read()

            template = template.replace(f"{{{{{var}}}}}", val)

        # handle recursive templates (dicts)
        for var, val in content["variables"].items():
            if isinstance(val, dict) and "template" in list(val.values())[0]:
                render_html(
                    val,
                    output_dir=f"{output_dir}/{page}",
                    var_name=var,
                    parent_template=template,
                )
                break
        else:
            output_path = os.path.join(root_dir, f"{output_dir}/{page}.html")
            with open(output_path, "w") as f:
                f.write(template)


render_html(site_template)
