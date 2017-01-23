# Wireframes for UN/ARMS public site

## Things To Do

* Fork and modify Cactus [so a static-url setting can be used](https://github.com/eudicots/Cactus/issues/236). In the meantime, before deploying to the [GitHub pages-powered prototype host](https://hypertexthero.github.io/unarmsdev/), [open `docs` folder and search–and-replace:  
 `src="/static/` with `src="/unarmsdev/static/`  
 …and…  
 `href="/static/` with `href="/unarmsdev/static/` 
* Consolidate about pages into single or less pages, and finalize other information architecture.
* Google form to save applicant info in both PDF and CSV formats and email to ARMS staff.
* Decided how to implement **local site search** (look at local JS search plugins for jQuery?) - see <https://www.nationalarchives.gov.uk/>
* Facebook, Flickr, (UN/ARMS Instagram with pokémon pictures? :) feeds and 'About UN/ARMS' with a strong image on homepage.
* Find **concepts/pictures/images for each page**
* Further updates to visual design and look and feel with CSS. Look at [Atom.io](http://flight-manual.atom.io/getting-started/sections/why-atom/) page for inspiration
* Fix tab fragment navigation on `/records/index.hml` - see http://stackoverflow.com/a/12131590
* Find out why **404 page template is not working**