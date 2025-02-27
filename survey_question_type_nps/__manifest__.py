# Copyright 2018 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Survey nps question type",
    "summary": """
        This module add nps rating as question type for survey page""",
    "version": "17.0.1.0.0",
    "license": "AGPL-3",
    "author": "ACSONE SA/NV,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/survey",
    "depends": ["survey"],
    "data": [
        "views/survey_question.xml",
        "templates/survey_template.xml",
    ],
    "assets": {
        "survey.survey_assets": [
            "/survey_question_type_nps/static/src/js/survey.js",
            "/survey_question_type_nps/static/src/scss/parameters.scss",
            "/survey_question_type_nps/static/src/scss/survey.scss",
        ],
    },
    "demo": [],
}
