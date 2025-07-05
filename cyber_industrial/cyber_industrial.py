### core project imports...
import reflex as rx

### configuration imports...
from rxconfig import config
### page route imports...
from cyber_industrial.page.home import home
from cyber_industrial.page.signup import signup
from cyber_industrial.page.login import login
from cyber_industrial.page.logcollection import logcollection
from cyber_industrial.page.datfileupdate import datfileupdate
from cyber_industrial.page.imagecollection import imagecollection
from cyber_industrial.page.databasemods import databasemods
from cyber_industrial.page.analytics import analytics


### application instantiation...
app = rx.App()

### application page routing...
app.add_page(home, route="/")
app.add_page(login, route="/login")
app.add_page(logcollection, route="/logcollection")
app.add_page(datfileupdate, route="/datfileupdate")
app.add_page(databasemods, route="/databasemods")
app.add_page(imagecollection, route="/imagecollection")
app.add_page(analytics, route="/analytics")
app.add_page(signup, route="/signup")