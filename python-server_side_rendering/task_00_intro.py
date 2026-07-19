#!/usr/bin/python3
"""Module for generating personalized invitation files from a template."""


def generate_invitations(template, attendees):
    """Generate invitation files from a template and a list of attendees.

    Args:
        template (str): The invitation template containing placeholders.
        attendees (list): A list of dictionaries with attendee data.

    Returns:
        None
    """
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
            isinstance(attendee, dict) for attendee in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        output_content = template
        for placeholder in placeholders:
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            output_content = output_content.replace(
                "{" + placeholder + "}", str(value))

        output_filename = "output_{}.txt".format(index)
        with open(output_filename, "w") as output_file:
            output_file.write(output_content)
