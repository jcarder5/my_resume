from flask_script import Manager
from professorbase import app, db, Professor, Course

manager = Manager(app)


# reset the database and create some initial data
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    debra = Professor(name='Debra Dragone', department='Accounting')
    jackson = Professor(name='Jackson Gillespie', department='Accounting')
    course1 = Course(name='Cost Accounting', number=327, description="Process, job order and standard costing; variable and absorption costing; budgeting, decentralization, and transfer pricing; and cost analysis for managerial applications. PREREQ: ACCT208. RESTRICTIONS: Requires sophomore status.")
    course2 = Course(name='Managerial Accounting', number=208, description="Introduction to managerial accounting. Topics: manufacturing accounting, cost-volume-profit analysis, job-order accounting, budgeting, standard costs and variance analysis, contribution approach to decision analysis, absorption and variable costing. PREREQ: ACCT207. RESTRICTIONS: Not open to freshmen. Requires a grade of C- or better in ACCT207.")
    course3 = Course(name='Intermediate Accounting', number=315, description="In-depth coverage of financial accounting. Topics include: environment and conceptual framework of financial accounting; review of the accounting process; preparation of financial statements; recognition and measurement of current assets, property, plant and equipment and current liabilities. PREREQ: ACCT207, ACCT208. RESTRICTIONS: Requires sophomore status.")
    course4 = Course(name='Intermediate Accounting II', number=316, description="Continuation of ACCT315. Topics include: recognition and measurement of investments, long-term liabilities and stockholders' equity; dilutive securities and earning per share calculations; revenue recognition; accounting for income taxes, pensions and leases; accounting changes and error analysis; financial reporting and changing prices; preparation of the statement of cash flows; and disclosure requirements in financial reporting. PREREQ:ACCT315. RESTRICTIONS: Requires junior status and a grade of C- or better in ACCT315.")
    db.session.add(debra)
    db.session.add(jackson)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
