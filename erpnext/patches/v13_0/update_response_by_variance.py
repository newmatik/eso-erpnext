# Copyright (c) 2020, Frappe and Contributors
# License: GNU General Public License v3. See license.txt


import frappe


def execute():
	if frappe.db.exists("DocType", "Issue") and frappe.db.count("Issue"):
		invalid_issues = frappe.db.sql(
			"""
			SELECT
				`name`,
				`response_by_variance`,
				TIMESTAMPDIFF(SECOND, `first_responded_on`, `response_by`) AS variance
			FROM `tabIssue`
			WHERE `first_responded_on` IS NOT NULL
				AND `response_by_variance` < 0
			""",
			as_dict=True,
		)

		# issues which has response_by_variance set as -ve
		# but diff between first_responded_on & response_by is +ve i.e SLA isn't failed
		invalid_issues = [d for d in invalid_issues if d.get("variance") > 0]

		for issue in invalid_issues:
			frappe.db.set_value(
				"Issue",
				issue.get("name"),
				"response_by_variance",
				issue.get("variance"),
				update_modified=False,
			)

		invalid_issues = frappe.db.sql(
			"""
			SELECT
				`name`,
				`resolution_by_variance`,
				TIMESTAMPDIFF(SECOND, `resolution_date`, `resolution_by`) AS variance
			FROM `tabIssue`
			WHERE `resolution_date` IS NOT NULL
				AND `resolution_by_variance` < 0
			""",
			as_dict=True,
		)

		# issues which has resolution_by_variance set as -ve
		# but diff between resolution_date & resolution_by is +ve i.e SLA isn't failed
		invalid_issues = [d for d in invalid_issues if d.get("variance") > 0]

		for issue in invalid_issues:
			frappe.db.set_value(
				"Issue",
				issue.get("name"),
				"resolution_by_variance",
				issue.get("variance"),
				update_modified=False,
			)
