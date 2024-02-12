# Generated by Django 5.0.1 on 2024-01-31 13:31

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.manager
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=60)),
                ('text', models.TextField()),
                ('private', models.BooleanField(default=False)),
                ('language', models.CharField(choices=[('ABAP', 'ABAP'), ('AMDGPU', 'AMDGPU'), ('APL', 'APL'), ('ABNF', 'ABNF'), ('ActionScript 3', 'ActionScript 3'), ('ActionScript', 'ActionScript'), ('Ada', 'Ada'), ('ADL', 'ADL'), ('Agda', 'Agda'), ('Aheui', 'Aheui'), ('Alloy', 'Alloy'), ('AmbientTalk', 'AmbientTalk'), ('Ampl', 'Ampl'), ('HTML + Angular2', 'HTML + Angular2'), ('Angular2', 'Angular2'), ('ANTLR With ActionScript Target', 'ANTLR With ActionScript Target'), ('ANTLR With C# Target', 'ANTLR With C# Target'), ('ANTLR With CPP Target', 'ANTLR With CPP Target'), ('ANTLR With Java Target', 'ANTLR With Java Target'), ('ANTLR', 'ANTLR'), ('ANTLR With ObjectiveC Target', 'ANTLR With ObjectiveC Target'), ('ANTLR With Perl Target', 'ANTLR With Perl Target'), ('ANTLR With Python Target', 'ANTLR With Python Target'), ('ANTLR With Ruby Target', 'ANTLR With Ruby Target'), ('ApacheConf', 'ApacheConf'), ('AppleScript', 'AppleScript'), ('Arduino', 'Arduino'), ('Arrow', 'Arrow'), ('Arturo', 'Arturo'), ('ASCII armored', 'ASCII armored'), ('ASN.1', 'ASN.1'), ('AspectJ', 'AspectJ'), ('Asymptote', 'Asymptote'), ('Augeas', 'Augeas'), ('AutoIt', 'AutoIt'), ('autohotkey', 'autohotkey'), ('Awk', 'Awk'), ('BBC Basic', 'BBC Basic'), ('BBCode', 'BBCode'), ('BC', 'BC'), ('BQN', 'BQN'), ('BST', 'BST'), ('BARE', 'BARE'), ('Base Makefile', 'Base Makefile'), ('Bash', 'Bash'), ('Bash Session', 'Bash Session'), ('Batchfile', 'Batchfile'), ('Bdd', 'Bdd'), ('Befunge', 'Befunge'), ('Berry', 'Berry'), ('BibTeX', 'BibTeX'), ('BlitzBasic', 'BlitzBasic'), ('BlitzMax', 'BlitzMax'), ('Blueprint', 'Blueprint'), ('BNF', 'BNF'), ('Boa', 'Boa'), ('Boo', 'Boo'), ('Boogie', 'Boogie'), ('Brainfuck', 'Brainfuck'), ('BUGS', 'BUGS'), ('CAmkES', 'CAmkES'), ('C', 'C'), ('CMake', 'CMake'), ('c-objdump', 'c-objdump'), ('CPSA', 'CPSA'), ('CSS+UL4', 'CSS+UL4'), ('aspx-cs', 'aspx-cs'), ('C#', 'C#'), ('ca65 assembler', 'ca65 assembler'), ('cADL', 'cADL'), ('CapDL', 'CapDL'), ("Cap'n Proto", "Cap'n Proto"), ('Carbon', 'Carbon'), ('CBM BASIC V2', 'CBM BASIC V2'), ('CDDL', 'CDDL'), ('Ceylon', 'Ceylon'), ('CFEngine3', 'CFEngine3'), ('ChaiScript', 'ChaiScript'), ('Chapel', 'Chapel'), ('Charmci', 'Charmci'), ('HTML+Cheetah', 'HTML+Cheetah'), ('JavaScript+Cheetah', 'JavaScript+Cheetah'), ('Cheetah', 'Cheetah'), ('XML+Cheetah', 'XML+Cheetah'), ('Cirru', 'Cirru'), ('Clay', 'Clay'), ('Clean', 'Clean'), ('Clojure', 'Clojure'), ('ClojureScript', 'ClojureScript'), ('COBOLFree', 'COBOLFree'), ('COBOL', 'COBOL'), ('CoffeeScript', 'CoffeeScript'), ('Coldfusion CFC', 'Coldfusion CFC'), ('Coldfusion HTML', 'Coldfusion HTML'), ('cfstatement', 'cfstatement'), ('COMAL-80', 'COMAL-80'), ('Common Lisp', 'Common Lisp'), ('Component Pascal', 'Component Pascal'), ('Coq', 'Coq'), ('cplint', 'cplint'), ('C++', 'C++'), ('cpp-objdump', 'cpp-objdump'), ('Crmsh', 'Crmsh'), ('Croc', 'Croc'), ('Cryptol', 'Cryptol'), ('Crystal', 'Crystal'), ('Csound Document', 'Csound Document'), ('Csound Orchestra', 'Csound Orchestra'), ('Csound Score', 'Csound Score'), ('CSS+Django/Jinja', 'CSS+Django/Jinja'), ('CSS+Ruby', 'CSS+Ruby'), ('CSS+Genshi Text', 'CSS+Genshi Text'), ('CSS', 'CSS'), ('CSS+PHP', 'CSS+PHP'), ('CSS+Smarty', 'CSS+Smarty'), ('CUDA', 'CUDA'), ('Cypher', 'Cypher'), ('Cython', 'Cython'), ('D', 'D'), ('d-objdump', 'd-objdump'), ('Darcs Patch', 'Darcs Patch'), ('Dart', 'Dart'), ('DASM16', 'DASM16'), ('Dax', 'Dax'), ('Debian Control file', 'Debian Control file'), ('Delphi', 'Delphi'), ('Desktop file', 'Desktop file'), ('Devicetree', 'Devicetree'), ('dg', 'dg'), ('Diff', 'Diff'), ('Django/Jinja', 'Django/Jinja'), ('Zone', 'Zone'), ('Docker', 'Docker'), ('DTD', 'DTD'), ('Duel', 'Duel'), ('Dylan session', 'Dylan session'), ('Dylan', 'Dylan'), ('DylanLID', 'DylanLID'), ('ECL', 'ECL'), ('eC', 'eC'), ('Earl Grey', 'Earl Grey'), ('Easytrieve', 'Easytrieve'), ('EBNF', 'EBNF'), ('Eiffel', 'Eiffel'), ('Elixir iex session', 'Elixir iex session'), ('Elixir', 'Elixir'), ('Elm', 'Elm'), ('Elpi', 'Elpi'), ('EmacsLisp', 'EmacsLisp'), ('E-mail', 'E-mail'), ('ERB', 'ERB'), ('Erlang', 'Erlang'), ('Erlang erl session', 'Erlang erl session'), ('HTML+Evoque', 'HTML+Evoque'), ('Evoque', 'Evoque'), ('XML+Evoque', 'XML+Evoque'), ('execline', 'execline'), ('Ezhil', 'Ezhil'), ('F#', 'F#'), ('FStar', 'FStar'), ('Factor', 'Factor'), ('Fancy', 'Fancy'), ('Fantom', 'Fantom'), ('Felix', 'Felix'), ('Fennel', 'Fennel'), ('Fift', 'Fift'), ('Fish', 'Fish'), ('Flatline', 'Flatline'), ('FloScript', 'FloScript'), ('Forth', 'Forth'), ('FortranFixed', 'FortranFixed'), ('Fortran', 'Fortran'), ('FoxPro', 'FoxPro'), ('Freefem', 'Freefem'), ('FunC', 'FunC'), ('Futhark', 'Futhark'), ('GAP session', 'GAP session'), ('GAP', 'GAP'), ('GDScript', 'GDScript'), ('GLSL', 'GLSL'), ('GSQL', 'GSQL'), ('GAS', 'GAS'), ('g-code', 'g-code'), ('Genshi', 'Genshi'), ('Genshi Text', 'Genshi Text'), ('Gettext Catalog', 'Gettext Catalog'), ('Gherkin', 'Gherkin'), ('Gnuplot', 'Gnuplot'), ('Go', 'Go'), ('Golo', 'Golo'), ('GoodData-CL', 'GoodData-CL'), ('Gosu', 'Gosu'), ('Gosu Template', 'Gosu Template'), ('GraphQL', 'GraphQL'), ('Graphviz', 'Graphviz'), ('Groff', 'Groff'), ('Groovy', 'Groovy'), ('HLSL', 'HLSL'), ('HTML+UL4', 'HTML+UL4'), ('Haml', 'Haml'), ('HTML+Handlebars', 'HTML+Handlebars'), ('Handlebars', 'Handlebars'), ('Haskell', 'Haskell'), ('Haxe', 'Haxe'), ('Hexdump', 'Hexdump'), ('HSAIL', 'HSAIL'), ('Hspec', 'Hspec'), ('HTML+Django/Jinja', 'HTML+Django/Jinja'), ('HTML+Genshi', 'HTML+Genshi'), ('HTML', 'HTML'), ('HTML+PHP', 'HTML+PHP'), ('HTML+Smarty', 'HTML+Smarty'), ('HTTP', 'HTTP'), ('Hxml', 'Hxml'), ('Hy', 'Hy'), ('Hybris', 'Hybris'), ('IDL', 'IDL'), ('Icon', 'Icon'), ('Idris', 'Idris'), ('Igor', 'Igor'), ('Inform 6', 'Inform 6'), ('Inform 6 template', 'Inform 6 template'), ('Inform 7', 'Inform 7'), ('INI', 'INI'), ('Io', 'Io'), ('Ioke', 'Ioke'), ('IRC logs', 'IRC logs'), ('Isabelle', 'Isabelle'), ('J', 'J'), ('JMESPath', 'JMESPath'), ('JSLT', 'JSLT'), ('JAGS', 'JAGS'), ('Jasmin', 'Jasmin'), ('Java', 'Java'), ('JavaScript+Django/Jinja', 'JavaScript+Django/Jinja'), ('JavaScript+Ruby', 'JavaScript+Ruby'), ('JavaScript+Genshi Text', 'JavaScript+Genshi Text'), ('JavaScript', 'JavaScript'), ('JavaScript+PHP', 'JavaScript+PHP'), ('JavaScript+Smarty', 'JavaScript+Smarty'), ('Javascript+UL4', 'Javascript+UL4'), ('JCL', 'JCL'), ('JSGF', 'JSGF'), ('JSONBareObject', 'JSONBareObject'), ('JSON-LD', 'JSON-LD'), ('JSON', 'JSON'), ('Jsonnet', 'Jsonnet'), ('Java Server Page', 'Java Server Page'), ('JSX', 'JSX'), ('Julia console', 'Julia console'), ('Julia', 'Julia'), ('Juttle', 'Juttle'), ('K', 'K'), ('Kal', 'Kal'), ('Kconfig', 'Kconfig'), ('Kernel log', 'Kernel log'), ('Koka', 'Koka'), ('Kotlin', 'Kotlin'), ('Kuin', 'Kuin'), ('Kusto', 'Kusto'), ('LSL', 'LSL'), ('CSS+Lasso', 'CSS+Lasso'), ('HTML+Lasso', 'HTML+Lasso'), ('JavaScript+Lasso', 'JavaScript+Lasso'), ('Lasso', 'Lasso'), ('XML+Lasso', 'XML+Lasso'), ('LDAP configuration file', 'LDAP configuration file'), ('LDIF', 'LDIF'), ('Lean', 'Lean'), ('LessCss', 'LessCss'), ('Lighttpd configuration file', 'Lighttpd configuration file'), ('LilyPond', 'LilyPond'), ('Limbo', 'Limbo'), ('liquid', 'liquid'), ('Literate Agda', 'Literate Agda'), ('Literate Cryptol', 'Literate Cryptol'), ('Literate Haskell', 'Literate Haskell'), ('Literate Idris', 'Literate Idris'), ('LiveScript', 'LiveScript'), ('LLVM', 'LLVM'), ('LLVM-MIR Body', 'LLVM-MIR Body'), ('LLVM-MIR', 'LLVM-MIR'), ('Logos', 'Logos'), ('Logtalk', 'Logtalk'), ('Lua', 'Lua'), ('MCFunction', 'MCFunction'), ('MCSchema', 'MCSchema'), ('MIME', 'MIME'), ('MIPS', 'MIPS'), ('MOOCode', 'MOOCode'), ('MSDOS Session', 'MSDOS Session'), ('Macaulay2', 'Macaulay2'), ('Makefile', 'Makefile'), ('CSS+Mako', 'CSS+Mako'), ('HTML+Mako', 'HTML+Mako'), ('JavaScript+Mako', 'JavaScript+Mako'), ('Mako', 'Mako'), ('XML+Mako', 'XML+Mako'), ('MAQL', 'MAQL'), ('Markdown', 'Markdown'), ('Mask', 'Mask'), ('Mason', 'Mason'), ('Mathematica', 'Mathematica'), ('Matlab', 'Matlab'), ('Matlab session', 'Matlab session'), ('Maxima', 'Maxima'), ('Meson', 'Meson'), ('MiniD', 'MiniD'), ('MiniScript', 'MiniScript'), ('Modelica', 'Modelica'), ('Modula-2', 'Modula-2'), ('MoinMoin/Trac Wiki markup', 'MoinMoin/Trac Wiki markup'), ('Monkey', 'Monkey'), ('Monte', 'Monte'), ('MoonScript', 'MoonScript'), ('Mosel', 'Mosel'), ('CSS+mozpreproc', 'CSS+mozpreproc'), ('mozhashpreproc', 'mozhashpreproc'), ('Javascript+mozpreproc', 'Javascript+mozpreproc'), ('mozpercentpreproc', 'mozpercentpreproc'), ('XUL+mozpreproc', 'XUL+mozpreproc'), ('MQL', 'MQL'), ('Mscgen', 'Mscgen'), ('MuPAD', 'MuPAD'), ('MXML', 'MXML'), ('MySQL', 'MySQL'), ('CSS+Myghty', 'CSS+Myghty'), ('HTML+Myghty', 'HTML+Myghty'), ('JavaScript+Myghty', 'JavaScript+Myghty'), ('Myghty', 'Myghty'), ('XML+Myghty', 'XML+Myghty'), ('NCL', 'NCL'), ('NSIS', 'NSIS'), ('NASM', 'NASM'), ('objdump-nasm', 'objdump-nasm'), ('Nemerle', 'Nemerle'), ('nesC', 'nesC'), ('NestedText', 'NestedText'), ('NewLisp', 'NewLisp'), ('Newspeak', 'Newspeak'), ('Nginx configuration file', 'Nginx configuration file'), ('Nimrod', 'Nimrod'), ('Nit', 'Nit'), ('Nix', 'Nix'), ('Node.js REPL console session', 'Node.js REPL console session'), ('Notmuch', 'Notmuch'), ('NuSMV', 'NuSMV'), ('NumPy', 'NumPy'), ('objdump', 'objdump'), ('Objective-C', 'Objective-C'), ('Objective-C++', 'Objective-C++'), ('Objective-J', 'Objective-J'), ('OCaml', 'OCaml'), ('Octave', 'Octave'), ('ODIN', 'ODIN'), ('OMG Interface Definition Language', 'OMG Interface Definition Language'), ('Ooc', 'Ooc'), ('Opa', 'Opa'), ('OpenEdge ABL', 'OpenEdge ABL'), ('OpenSCAD', 'OpenSCAD'), ('Text output', 'Text output'), ('PacmanConf', 'PacmanConf'), ('Pan', 'Pan'), ('ParaSail', 'ParaSail'), ('Pawn', 'Pawn'), ('PEG', 'PEG'), ('Perl6', 'Perl6'), ('Perl', 'Perl'), ('Phix', 'Phix'), ('PHP', 'PHP'), ('Pig', 'Pig'), ('Pike', 'Pike'), ('PkgConfig', 'PkgConfig'), ('PL/pgSQL', 'PL/pgSQL'), ('Pointless', 'Pointless'), ('Pony', 'Pony'), ('Portugol', 'Portugol'), ('PostScript', 'PostScript'), ('PostgreSQL console (psql)', 'PostgreSQL console (psql)'), ('PostgreSQL EXPLAIN dialect', 'PostgreSQL EXPLAIN dialect'), ('PostgreSQL SQL dialect', 'PostgreSQL SQL dialect'), ('POVRay', 'POVRay'), ('PowerShell', 'PowerShell'), ('PowerShell Session', 'PowerShell Session'), ('Praat', 'Praat'), ('Procfile', 'Procfile'), ('Prolog', 'Prolog'), ('PromQL', 'PromQL'), ('Properties', 'Properties'), ('Protocol Buffer', 'Protocol Buffer'), ('PRQL', 'PRQL'), ('PsySH console session for PHP', 'PsySH console session for PHP'), ('PTX', 'PTX'), ('Pug', 'Pug'), ('Puppet', 'Puppet'), ('PyPy Log', 'PyPy Log'), ('Python 2.x', 'Python 2.x'), ('Python 2.x Traceback', 'Python 2.x Traceback'), ('Python console session', 'Python console session'), ('Python', 'Python'), ('Python Traceback', 'Python Traceback'), ('Python+UL4', 'Python+UL4'), ('QBasic', 'QBasic'), ('Q', 'Q'), ('QVTO', 'QVTO'), ('Qlik', 'Qlik'), ('QML', 'QML'), ('RConsole', 'RConsole'), ('Relax-NG Compact', 'Relax-NG Compact'), ('RPMSpec', 'RPMSpec'), ('Racket', 'Racket'), ('Ragel in C Host', 'Ragel in C Host'), ('Ragel in CPP Host', 'Ragel in CPP Host'), ('Ragel in D Host', 'Ragel in D Host'), ('Embedded Ragel', 'Embedded Ragel'), ('Ragel in Java Host', 'Ragel in Java Host'), ('Ragel', 'Ragel'), ('Ragel in Objective C Host', 'Ragel in Objective C Host'), ('Ragel in Ruby Host', 'Ragel in Ruby Host'), ('Raw token data', 'Raw token data'), ('Rd', 'Rd'), ('ReasonML', 'ReasonML'), ('REBOL', 'REBOL'), ('Red', 'Red'), ('Redcode', 'Redcode'), ('reg', 'reg'), ('ResourceBundle', 'ResourceBundle'), ('Rexx', 'Rexx'), ('RHTML', 'RHTML'), ('Ride', 'Ride'), ('Rita', 'Rita'), ('Roboconf Graph', 'Roboconf Graph'), ('Roboconf Instances', 'Roboconf Instances'), ('RobotFramework', 'RobotFramework'), ('RQL', 'RQL'), ('RSL', 'RSL'), ('reStructuredText', 'reStructuredText'), ('TrafficScript', 'TrafficScript'), ('Ruby irb session', 'Ruby irb session'), ('Ruby', 'Ruby'), ('Rust', 'Rust'), ('SAS', 'SAS'), ('S', 'S'), ('Standard ML', 'Standard ML'), ('SNBT', 'SNBT'), ('SARL', 'SARL'), ('Sass', 'Sass'), ('Savi', 'Savi'), ('Scala', 'Scala'), ('Scaml', 'Scaml'), ('scdoc', 'scdoc'), ('Scheme', 'Scheme'), ('Scilab', 'Scilab'), ('SCSS', 'SCSS'), ('Sed', 'Sed'), ('ShExC', 'ShExC'), ('Shen', 'Shen'), ('Sieve', 'Sieve'), ('Silver', 'Silver'), ('Singularity', 'Singularity'), ('Slash', 'Slash'), ('Slim', 'Slim'), ('Slurm', 'Slurm'), ('Smali', 'Smali'), ('Smalltalk', 'Smalltalk'), ('SmartGameFormat', 'SmartGameFormat'), ('Smarty', 'Smarty'), ('Smithy', 'Smithy'), ('Snobol', 'Snobol'), ('Snowball', 'Snowball'), ('Solidity', 'Solidity'), ('Sophia', 'Sophia'), ('SourcePawn', 'SourcePawn'), ('Debian Sourcelist', 'Debian Sourcelist'), ('SPARQL', 'SPARQL'), ('Spice', 'Spice'), ('SQL+Jinja', 'SQL+Jinja'), ('SQL', 'SQL'), ('sqlite3con', 'sqlite3con'), ('SquidConf', 'SquidConf'), ('Srcinfo', 'Srcinfo'), ('Scalate Server Page', 'Scalate Server Page'), ('Stan', 'Stan'), ('Stata', 'Stata'), ('SuperCollider', 'SuperCollider'), ('Swift', 'Swift'), ('SWIG', 'SWIG'), ('systemverilog', 'systemverilog'), ('Systemd', 'Systemd'), ('TAP', 'TAP'), ('Typographic Number Theory', 'Typographic Number Theory'), ('TOML', 'TOML'), ('TADS 3', 'TADS 3'), ('Tal', 'Tal'), ('TASM', 'TASM'), ('Tcl', 'Tcl'), ('Tcsh', 'Tcsh'), ('Tcsh Session', 'Tcsh Session'), ('Tea', 'Tea'), ('teal', 'teal'), ('Tera Term macro', 'Tera Term macro'), ('Termcap', 'Termcap'), ('Terminfo', 'Terminfo'), ('Terraform', 'Terraform'), ('TeX', 'TeX'), ('Text only', 'Text only'), ('ThingsDB', 'ThingsDB'), ('Thrift', 'Thrift'), ('tiddler', 'tiddler'), ('Tl-b', 'Tl-b'), ('TLS Presentation Language', 'TLS Presentation Language'), ('Todotxt', 'Todotxt'), ('Transact-SQL', 'Transact-SQL'), ('Treetop', 'Treetop'), ('Turtle', 'Turtle'), ('HTML+Twig', 'HTML+Twig'), ('Twig', 'Twig'), ('TypeScript', 'TypeScript'), ('TypoScriptCssData', 'TypoScriptCssData'), ('TypoScriptHtmlData', 'TypoScriptHtmlData'), ('TypoScript', 'TypoScript'), ('UL4', 'UL4'), ('ucode', 'ucode'), ('Unicon', 'Unicon'), ('Unix/Linux config files', 'Unix/Linux config files'), ('UrbiScript', 'UrbiScript'), ('urlencoded', 'urlencoded'), ('USD', 'USD'), ('VBScript', 'VBScript'), ('VCL', 'VCL'), ('VCLSnippets', 'VCLSnippets'), ('VCTreeStatus', 'VCTreeStatus'), ('VGL', 'VGL'), ('Vala', 'Vala'), ('aspx-vb', 'aspx-vb'), ('VB.net', 'VB.net'), ('HTML+Velocity', 'HTML+Velocity'), ('Velocity', 'Velocity'), ('XML+Velocity', 'XML+Velocity'), ('Verifpal', 'Verifpal'), ('verilog', 'verilog'), ('vhdl', 'vhdl'), ('VimL', 'VimL'), ('Visual Prolog Grammar', 'Visual Prolog Grammar'), ('Visual Prolog', 'Visual Prolog'), ('Vyper', 'Vyper'), ('WDiff', 'WDiff'), ('WebAssembly', 'WebAssembly'), ('Web IDL', 'Web IDL'), ('WebGPU Shading Language', 'WebGPU Shading Language'), ('Whiley', 'Whiley'), ('Wikitext', 'Wikitext'), ('World of Warcraft TOC', 'World of Warcraft TOC'), ('Wren', 'Wren'), ('X10', 'X10'), ('XML+UL4', 'XML+UL4'), ('XQuery', 'XQuery'), ('XML+Django/Jinja', 'XML+Django/Jinja'), ('XML+Ruby', 'XML+Ruby'), ('XML', 'XML'), ('XML+PHP', 'XML+PHP'), ('XML+Smarty', 'XML+Smarty'), ('Xorg', 'Xorg'), ('X++', 'X++'), ('XSLT', 'XSLT'), ('Xtend', 'Xtend'), ('xtlang', 'xtlang'), ('YAML+Jinja', 'YAML+Jinja'), ('YAML', 'YAML'), ('YANG', 'YANG'), ('YARA', 'YARA'), ('Zeek', 'Zeek'), ('Zephir', 'Zephir'), ('Zig', 'Zig'), ('ANSYS parametric design language', 'ANSYS parametric design language')], max_length=53)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('token', models.CharField(max_length=15, unique=True)),
            ],
            managers=[
                ('privates', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
