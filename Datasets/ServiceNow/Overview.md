**Common User Interfaces**

- Workspaces: a suite of tools displayed in a single-pane view
- Lists: displays records from a table in the Platform
- Forms: displays fields from one record, where users can view and edit the record data.
	- Related Lists: records in tables that have a relationship to the current record
- Dashboards:  is a custom arrangement of widgets, you can share with multiple users
- Knowledge Articles: are uploaded to the Platform in specific categories to help platform users
- Service Catalog:  can view and request services and product offerings

**User Access and Personas**
- System Administrator: access to all platform features. applications, functions and data  
- Specialized Administrator: specific admin access
- Process User: fulfil ITIL activities associated with the ITIL workflow 
- Approver: can perform all requestor actions and allows users to view/modify approval record directed to them 
- Requester: do not have roles but can submit and manage their own requests, access public pages, etc
- Users: are represented by a record on the User `sys_user` table 
- Group: a collection of users represented by a record on the Group `sys_user_group` table 
- Role: used to define access at the application module, and/or Access Control List (ACL), roles can contain other roles, group and users. Represented by a record on the Role `sys_user_role` table.
- Delegated developers: non-administrator users and group which are assigned one or more permissions to develop applications 

**Types of visualizations available**:
- Basic Charts: Donut/pie/semi-donut/Funnel/List
- 2D charts: Bar/Column/Histogram/Pareto/Box
- Times series: Area/Column/Line/Scatter/Spline/Step
- Multi-dimension: Pivot-table/Heat-map/Bubble/Calendar
- Scores: Single Score/Dial/Gauge/Score Card