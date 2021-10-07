import frappe, json

def execute():
    
    data = frappe.db.sql("""
    select data
    from `tabVersion`
    where ref_doctype = "Item"
    """,as_list=True)

    for d in data: 
        d = json.loads(d[0])
        # print(d['added'][0][1]['added_on'] +" : " +d['added'][0][1]['name'])
        frappe.db.sql("""
        update `tabItem MPN`
        set added_on = '{0}'
        where name = '{1}';
        """.format(d['added'][0][1]['added_on'], d['added'][0][1]['name']))

        # frappe.db.set_value("Item MPN", d['added'][0][1]['name'], {'added_on':d['added'][0][1]['added_on']})