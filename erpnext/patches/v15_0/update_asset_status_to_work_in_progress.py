import frappe


def execute():
	# Skip patch if the is_composite_asset column no longer exists
	# (e.g. already removed by a later patch such as v16_0 asset type migration)
	if not frappe.db.has_column("Asset", "is_composite_asset"):
		return

	Asset = frappe.qb.DocType("Asset")
	query = (
		frappe.qb.update(Asset)
		.set(Asset.status, "Work In Progress")
		.where((Asset.docstatus == 0) & (Asset.is_composite_asset == 1))
	)
	query.run()
