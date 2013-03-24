The ZODB is a persistence system for Python objects. Persistent programming languages provide facilities that automatically write objects to disk and read them in again when they’re required by a running program.
The usual starting points are the pickle module, for converting objects into a string representation, and various database modules,
The ZODB comes with a few different classes that implement the Storage interface. Such classes handle the job of writing out Python objects to a physical storage medium, which can be a disk file (the FileStorage class), a BerkeleyDB file (BDBFullStorage), a relational database (DCOracleStorage), or some other medium. ZEO adds ClientStorage, a new Storage  that doesn’t write to physical media but just forwards all requests across a network to a server. The server, which is running an instance of the StorageServer class, simply acts as a front-end for some physical Storage class. It’s a fairly simple idea, but as we’ll see later on in this document, it opens up many possibilities.
About this guide¶

The primary author of this guide works on a project which uses the ZODB and ZEO as its primary storage technology. We use the ZODB to store process runs and operations, a catalog of available processes, user information, accounting information, and other data. Part of the goal of writing this document is to make our experience more widely available. 

Z Object Publishing Environment
ZMI (Zope Management Interface). 
What Is A Web Application?¶

A web application is a computer program that users invoke by using a web browser to contact a web server via the Internet. Users and browsers are typically unaware of the difference between a web server that fronts a statically-built website and one that fronts a web application.
Content Management System
Zope is a web application server.
Zope is family of related Python packages focussed on web technologies.
You can easily integrate Zope with diverse authentication and authorization systems, such as LDAP, Kerberos,
Zope separates the URL into its component “host”, “port” “path” and “query string” portions (‘http://www.zope.org‘, ‘8080’, ‘/Resources’ and ‘?batch_start=100’, respectively).
Each web request is treated as a separate transaction by the ZODB
Zope also works with other relational databases, including Oracle, PostgreSQL, Sybase, and MySQL.
bin\instance fg start stop debug
log var/log/instance.log

In a typical, non-object-oriented application, you will have two things:

    * Code. For example, a typical CGI-based web application may have a bit of logic in the form of a PHP script, which retrieves employee data from a database and displays tabular data to a user.
    * Data. For example, you may have employee data stored in a database, such as MySQL or Oracle, on which some code performs read or change operations. This data exists almost solely for the purpose of the code that operates upon it; without this code, the data holds little to no value.

In a typical object-oriented application, however, you will have one thing, and one thing only:

    * Objects. Simply stated, these objects are collections of code and data wrapped up together. For example, you may have an “Employee” object that represents an employee. It will contain data about the employee, such as a phone number, name, and address, much like the information that would be stored in a database. However, the object will also contain “logic,” or code, that can manipulate and display its data.

In a non-object-oriented application, your data is kept separate from your code. But in an object-oriented application, both your data and your code are stored in one or more objects, each of which represents a particular “thing”
Attribute inheritance,methods,objects,class.
Instead, the objects that Zope creates are stored in a database called the “Zope Object DataBase”, or the ZODB. In default configurations, the ZODB creates a file named “Data.fs” in which Zope stores its objects.

The ZMI uses three browser frames:

    * The left frame is called the Navigator Frame, which can be used to expand or collapse a view into the Zope object hierarchy, much like you would expand and collapse a view of files using a file tree widget like the one in Windows Explorer.
    * The right frame is called the Workspace Frame, which displays a particular view of the object you’re currently managing.
    * The top frame is called the Status Frame, which displays your user name (when logged in), as well as a drop-down list that performs various actions.

Creating Objects¶

The Zope Management Interface allows you to create new objects in your Zope instance. To add a new object, select an entry from the pull-down menu in the Workspace labeled “Select type to add...”. This pull-down menu is called the add list. 

In general, basic Zope objects take on one of three types of roles:

Content
    Zope objects like documents, images, and files hold different kinds of textual and binary data. In addition to objects in Zope containing content, Zope can work with content stored externally, such as information in a relational database.
Presentation
    You can control the look and feel of your site with Zope objects that act as web page “templates”. Zope comes with two facilities to help you manage presentation: Zope Page Templates (ZPT) and Document Templates (DTML). In the first part of the book we will only cover page templates and later on expand on document templates. If you already know HTML, page templates are easier to work with and more limited in their options. For some of the more advanced tasks DTML can be a better option as explained later on.
Logic
    Scripting business logic in Zope is done using Python. “Logic” is any kind of programming that does not involve presentation, but rather involves the carrying out of tasks such as changing objects, sending messages, testing conditions, and responding to events. 

Document Template Markup Language or short DTML.
“tag-based” scripting languages, like DTML, SSI, PHP, and JSP, encourage programmers to embed special tags into HTML that are, at best, 
Zope Page Templates (ZPTs) are typically used to create dynamic HTML pages.

The concept behind acquisition is simple:

    * Objects are situated inside other objects, and these objects act as their “containers”. For example, the container of a Page Template named “apage” inside a Folder “afolder” is the “afolder” folder.
    * Objects may acquire behavior from their containers.
an object’s inheritance hierarchy is always searched for behavior before its acquisition hierarchy. If the method or attribute is not found in the object’s inheritance hierarchy, then the acquisition hierarchy is searched.

Acquisition “goes both ways”: when you create an object in Zope, it has the capability to automatically acquire services. Additionally, it automatically provides services that other objects can acquire.

Acquisition is particularly useful for sharing information (such as headers and footers) between objects in different folders as well.

Zope will call the index_html object in the Zoo folder and display its results. You could instead use the more explicit URL:

http://localhost:8080/Zoo/index_html

In Python, dots are used to separate ids. This is the reason why Zope often uses ids like index_html instead of the more common index.html and why this example uses hello_world_pt instead of hello_world.pt.

Page Templates are a web page generation tool.They help programmers and designers collaborate in producing dynamic web pages for Zope web applications.

A good way to start building an application is to create a new Folder to hold all the objects and subfolders related to the application.

Zope maintains one or more of its own user databases.

AdvZPT==================
ScriptingZope.html
If you don’t want to use page templates for whatever reason DTML might work well. Likewise, if you want to dynamically create non-HTML text (like CSS stylesheets or email messages), DTML can help.
DTML is similar in function to “HTML-embedded” scripting languages such as JSP, PHP, or mod_perl. It differs from these facilities inasmuch as it will not allow you to create “inline” Python statements (if... then.. else..) in the way that JSP,

<dtml-in mySequence>

  this is a text inside the dtml-in tag block

</dtml-in> 

The target of the DTML tag ‘<dtml-in foo>’ is ‘foo’

<dtml-var bananas missing="We have no bananas">

<p>How many monkeys are there?</p>

<dtml-if expr="monkeys > monkey_limit">
  <p>There are too many monkeys!</p>
</dtml-if>

<dtml-in todo_list>
  <p><dtml-var description></p>
</dtml-in>

The Difference Between DTML Documents and DTML Methods¶

DTML Methods are used to carry out actions. They are presentation objects (as used in the vernacular of the `Using Basic Zope Objects`_ chapter). If you want to render the properties or attributes of another object like a DTML Document or a Folder, you will use a DTML Method. DTML Methods do not have their own properties.

DTML Documents are content objects (in the vernacular used in the chapter entitled `Using Basic Zope Objects`_). If you want to create a “stand-alone” text document, you might create a DTML Document object to hold the text. DTML Document objects have their own properties (attributes), unlike DTML Methods.

DTML Method vs. DTML Document¶

One of the most potentially confusing choices to make for Zope newbies is the choice between a DTML Method and a DTML Document. Unfortunately, many Zope newbies develop entire sites using one type of object only to discover that they should have used the other type. In general, keep the following items in mind when deciding upon which type to use:

    *

      Does the object require properties of its own? If so,

          use a DTML Document since DTML Methods have no inherent properties.

    *

      Does the object need to be called as a “page”? If so,

          consider using a DTML Document since it will be easier to control such items as page title by using properties.

    *

      Does the object need transparency to its context? If so,

          you should probably use a DTML Method since these objects act as though they are directly attached to their calling, or containing object.

Providing the credntial is called authentication.
After logging the providing the particular permission called Authorization

The most common and most flexible ORM in the Python world is SQLAlchemy.


sqlalchemy module.
Information in the table is stored in rows. The table’s column layout is called the schema

Oracle
    Oracle is arguably the most powerful and popular commercial relational database. It is, however, relatively expensive and complex. Oracle can be purchased or evaluated from the Oracle Website.
PostgreSQL
    PostgreSQL is a leading open source relational database with good support for SQL standards. You can find more information about PostgreSQL at the PostgreSQL web site.
MySQL
    MySQL is a fast open source relational database. You can find more information about MySQL at the MySQL web site.
SQL Server
    Microsoft’s full featured SQL Server for the Windows operating systems. For any serious use on Windows, it is preferable to Microsoft Access. Information from http://www.microsoft.com/sql/

Zope can connect to all the above-listed database systems; however, you should be satisfied that the database is running and operating in a satisfactory way on its own before attempting to connect it to Zope.

Database adapters
oracle - http://pypi.python.org/pypi?:action=browse&c=514
postgrace - http://www.zope.org/Members/matt/dco2
mssql - http://www.iinitd.org/software/psycopgpackage  
sql server- http://www.egenix.com/

A ZSQL Method has two functions: it generates SQL to send to the database and it converts the response from the database into an object. 

insert into employees (emp_id, first, last, salary) values
(<dtml-sqlvar emp_id type="int">,
 <dtml-sqlvar first type="string">,
 <dtml-sqlvar last type="string">,
 <dtml-sqlvar salary type="float">
)

As Zope is object oriented, a Z SQL method returns a Result object. All the result rows are packaged up into one object.

select * from employees
  where emp_id=<dtml-sqlvar emp_id type=int>

select * from employees
  where <dtml-sqltest salary op=gt type=float>

select * from employees
<dtml-sqlgroup where>
  <dtml-sqltest salary op=gt type=float optional>
<dtml-and>
  <dtml-sqltest first op="eq" type="nb" multiple optional>
<dtml-and>
  <dtml-sqltest last  op="eq" type="nb" multiple optional>
</dtml-sqlgroup>

To control caching, go to the Advanced tab of a SQL Method.

Virtual hosting is a way to serve many websites with one Zope server.

session
transient data object
    * Do not use SESSION to store REQUEST variables. They are already available in the REQUEST.
    * Do not store any data in SESSION that you can get from the Zope API. Its faster (and more secure) to get user Id from Zope’s Security Manager then it is from the SESSION object.


ZEO

ZEO is a system that allows you to share a Zope Object Database between more than one Zope process. By using ZEO, you may run multiple instances of Zope on a single computer or on multiple computers. 
Furthermore, if one Zope server fails or crashes, other servers can still service requests while you fix the broken one. ZEO takes care of making sure each Zope installation uses consistent information from the same Zope Object Database.

All of your ZEO clients must have the same third party Products installed and they must be the same version. This is necessary, or your third-party objects may behave abnormally or not work at all.
python /path/to/Zope/bin/mkzeoinstance.py /path/to/zeostorage
$ /path/to/zeostorage/bin/zeoctl start


The domain Name System, or DNS, is the Internet mechanism that translates computer names (like “www.zope.org”) into numeric addresses. This mechanism can map one name to many addresses.

One popular software solution for linux is called fake. Fake is a Linux-based utility that can make a backup computer take over for a failed primary computer by “faking out” network addresses. When used in conjunction with monitoring utilities like mon or heartbeat, fake can guarantee almost 100% up-time of your ZEO server.


python /path/to/Zope/utilities/ZODBTools/zeopack.py -h localhost -p 8001

ZEO servers do not have any in-memory cache for frequently or recently accessed items. Every request for an object from a ZEO client will cause a read from disk.

Maintaining the zope

Windows installing zope as a service.
 cd c:\Program Files\zope
> bin\lib\win32\PythonService.exe /register
> bin\python.exe ZServer\ZService.py --startup auto install

http://www.zope.org/Products
Database Cache¶

The most important is the database cache setting. To adjust these settings, visit the Control Panel and click on the Database link.

Appendix
http://docs.zope.org/zope2/zope2book/AppendixA.html

‘call’ tag syntax:

<dtml-call Variable|expr="Expression">
<dtml-comment>
 content is not executed and does not appear in the output.
</dtml-comment>

http://docs.zope.org/zope2/zope2book/BasicObject.html
