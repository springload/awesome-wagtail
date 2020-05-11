Awesome Wagtail [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [<img src="https://cdn.rawgit.com/springload/awesome-wagtail/ac912cc661a7099813f90545adffa6bb3e75216c/logo.svg" width="104" align="right" alt="Wagtail">](https://wagtail.io/)
===============

> A curated list of awesome packages, articles, and other cool resources from the Wagtail community.
> [Wagtail](https://wagtail.io/) is a Python CMS powered by Django, focusing on flexibility and user experience.

*You might also like [Awesome Django](https://gitlab.com/rosarior/awesome-django) and [Awesome Python](https://github.com/vinta/awesome-python). :snake:*

## Contents

- [General resources](#general-resources)
- [Apps](#apps)
  - [Blogging/news](#bloggingnews)
  - [Rich text editor extensions](#rich-text-editor-extensions)
  - [Widgets](#widgets)
  - [StreamField](#streamfield)
  - [Static site generation](#static-site-generation)
  - [Settings management](#settings-management)
  - [E-commerce](#e-commerce)
  - [SEO and SMO](#seo-and-smo)
  - [Analytics](#analytics)
  - [Customer experience](#customer-experience)
  - [Security](#security)
  - [Media](#media)
  - [Translations](#translations)
  - [Forms](#forms)
  - [Testing](#testing)
  - [Misc](#misc)
- [Tools](#tools)
- [Resources](#resources)
  - [Getting started](#getting-started)
  - [Articles](#articles)
  - [Recipes](#recipes)
  - [Presentations](#presentations)
  - [Podcasts](#podcasts)
  - [Videos](#videos)
  - [Showcases](#showcases)
  - [Lists](#lists)
  - [For Editors](#for-editors)
- [Community](#community)
- [Open-source sites](#open-source-sites)

## General resources

- [Official site](https://wagtail.io/)
- [GitHub repository](https://github.com/wagtail/wagtail)
- [Twitter account](https://twitter.com/wagtailcms)
- [Roadmap](https://github.com/wagtail/wagtail/projects/1)
- [PyPI classifiers for Wagtail](https://pypi.org/pypi?%3Aaction=list_classifiers)
- [Other resources](#resources)

## Apps

### Blogging/news

- [Puput](https://puput.readthedocs.org/) - Puput is a powerful and simple Django app to manage a blog. It uses the awesome Wagtail CMS as content management system.
- [wagtail_blog](https://github.com/thelabnyc/wagtail_blog) - A WordPress-like blog app implemented in Wagtail.
- [wagtailnews](https://github.com/takeflight/wagtailnews) - A plugin for Wagtail that provides news / blogging functionality.
- [wagtail-blog-app](https://github.com/Tivix/wagtail-blog-app) - A blog application for the Wagtail Django CMS.
- [Django Wagtail Feeds](https://github.com/chrisdev/django-wagtail-feeds) - Add support for RSS Feeds, Facebook Instant Articles and Apple News Publisher to your Wagtail CMS Projects.
- [CodeRed CMS](https://github.com/coderedcorp/coderedcms) - a professionally supported WordPress alternative for building marketing websites. Create pages, blogs, forms, and every Bootstrap 4 component in the wagtail admin out-of-the-box! [Learn more](https://www.coderedcorp.com/cms/) or [watch the lightning talk](https://www.youtube.com/watch?v=U1Y-jgeGh7g&t=228s).
- [Snotra_RSS](https://github.com/olopost/snotra_rss) - Snotra_RSS is an Atom and RSS news aggregator app for Wagtail.

### Rich text editor extensions

- [wagtail-readability](https://github.com/takeflight/wagtail-readability) - Test how readable the content you enter into Wagtail is.
- [wagtailembedder](https://github.com/springload/wagtailembedder) - Snippets embedder for Wagtail richtext fields.
- [Wagtail TinyMCE](https://github.com/isotoma/wagtailtinymce) - A TinyMCE editor integration for Wagtail.
- [Wagtail Froala](https://github.com/jaydensmith/wagtailfroala) - Extends Wagtail to use the Froala WYSIWYG editor in RichTextField/RichTextBlock.
- [Wagtail Medium Editor](https://github.com/dperetti/Django-wagtailmedium) - A customizable Medium Editor for Wagtail, with link anchors support.
- [WagtailDraftail](https://github.com/springload/wagtaildraftail) – Draft.js editor for Wagtail, built upon [Draftail](https://github.com/springload/draftail) and [draftjs_exporter](https://github.com/springload/draftjs_exporter).
- [wagtail-readinglevel](https://github.com/vixdigital/wagtail-readinglevel) – Wagtail plugin to determine the reading level of text input into a rich text field.

### Widgets

- [wagtailgmaps](https://github.com/springload/wagtailgmaps) - Simple Google Maps address formatter for Wagtail fields.
- [Wagtail-Geo-Widget](https://github.com/Frojd/wagtail-geo-widget) - Google Maps widget for the GeoDjango PointField field in Wagtail.
- [wagtail-leaflet-widget](https://github.com/icpac-igad/wagtail-leaflet-widget) - A Leaflet JS - OSM based wagtail geo-location widget.
- [wagtail-markdown](https://github.com/torchbox/wagtail-markdown) - Markdown fields and blocks for Wagtail.
- [wagtail-autocomplete](https://github.com/wagtail/wagtail-autocomplete) - Autocompleting choosers for `ForeignKey`, `ParentalKey`, and `ManyToMany` fields.
- [wagtail-instance-selector](https://github.com/ixc/wagtail-instance-selector) - A `ForeignKey` widget to create and select related items. Similar to Django's `raw_id_fields`.
- [wagtail-generic-choooser](https://github.com/wagtail/wagtail-generic-chooser) - provides base classes for building chooser popups and form widgets for the Wagtail admin, matching the look and feel of Wagtail's built-in choosers for pages, documents, snippets and images.

### StreamField

- [Wagtail FontAwesome](https://gitlab.com/alexgleason/wagtailfontawesome) - Add FontAwesome icons to StreamField.
- [Wagtail Commonblocks](https://github.com/springload/wagtailblocks) - Common StreamField blocks for Wagtail.
- [Wagtail SVGmap](https://github.com/City-of-Helsinki/wagtail-svgmap) - ImageMap functionality for Wagtail through inline SVGs.
- [Wagtail ClearStream](https://github.com/heymonkeyriot/wagtailclearstream) - An app to make Wagtail's StreamField more modular.
- [UWKM Streamfields](https://github.com/UWKM/uwkm_streamfields) – A basic set of Wagtail StreamField blocks for fun and profit.
- [wagtail-inventory](https://github.com/cfpb/wagtail-inventory) - Search Wagtail pages by the StreamField blocks they contain.
- [Wagtail Code Block](https://github.com/FlipperPA/wagtailcodeblock) - StreamField code blocks for the Wagtail CMS with real-time PrismJS Syntax Highlighting.
- [Wagtail Blocks](https://github.com/ibrahimawadhamid/wagtail_blocks) - A Collection of awesome Wagtail CMS stream-field blocks and Charts.
- [Wagtail UI Plus](https://github.com/davidcondenl/wagtailuiplus) - Several UI improvements to the Wagtail editor interface for StreamFields and StreamBlocks.
- [Wagtail Cache Block](https://github.com/AccordBox/wagtail_cache_block) - A templatetag which add HTML fragment cache to your StreamField block

### Static site generation

- [Wagtail-bakery](https://github.com/moorinteractive/wagtail-bakery) - A set of helpers for baking your Django Wagtail site out as flat files.
- [Wagtail-Netlify](https://github.com/tomdyson/wagtail-netlify) - Easilly publish your statically rendered Wagtail site to Netlify.

### Settings management

- [Wagtail-Constance](https://github.com/MechanisM/wagtail-constance) - django-constance integration for Wagtail CMS.
- [Wagtail-Flags](https://github.com/cfpb/wagtail-flags) - Feature flags for Wagtail sites.

### E-commerce

- [wagtailinvoices](https://github.com/SableWalnut/wagtailinvoices) - A Wagtail module for creating invoices.
- [longclaw](https://github.com/JamesRamm/longclaw) - A shop template for Wagtail CMS.
- [django-oscar-wagtail](https://github.com/LabD/django-oscar-wagtail) - Wagtail integration for Oscar Commerce (or Oscar Commerce integration for Wagtail?).

### SEO and SMO

- [wagtail-metadata](https://github.com/takeflight/wagtail-metadata) - A tool to assist with metadata for social media and search engines.
- [wagtail-metadata-mixin](https://github.com/bashu/wagtail-metadata-mixin) - OpenGraph, Twitter Card and Google+ snippet tags for Wagtail CMS pages.
- [wagtail-schema.org](https://github.com/takeflight/wagtail-schema.org) - Schema.org JSON-LD tags for Wagtail sites.
- [wagtail-opengraph-image-generator](https://github.com/candylabshq/wagtail-opengraph-image-generator) - Assists you in automatically creating Open Graph images for your Wagtail pages.
- [wagtail-redirect-importer](https://github.com/Frojd/wagtail-redirect-importer) - Your friendly neighborhood importer that lets you import redirects from different tabular data formats, such as .csv and .xls 

### Analytics

- [Wagtail Analytics](https://github.com/tomdyson/wagalytics) - A Google Analytics dashboard in your Wagtail admin.

### Customer experience

- [Wagtail Experiments](https://github.com/torchbox/wagtail-experiments) – A/B testing for Wagtail.
- [Wagtail Personalisation](https://github.com/LabD/wagtail-personalisation) - Personalisation module, enabling editors to create customised pages - or parts of pages - based on segments whose rules are configured directly in the admin interface.

### Security

- [wagtailenforcer](https://github.com/springload/wagtailenforcer) - If you need to enforce security protocols on your Wagtail site you've come to the right place.
- [wagtail-yubikey](https://github.com/ahopkins/wagtail-yubikey) - Enable YubiKey two factor authentication on Wagtail admin panel.
- [wagtail-2fa](https://github.com/labd/wagtail-2fa) - Add two-factor authentication to Wagtail by integrating it with django-otp.

### Media

- [wagtailmedia](https://github.com/torchbox/wagtailmedia) - A Wagtail module for managing video and audio files within the admin.
- [Wagtail Alt Generator](https://github.com/marteinn/wagtail-alt-generator) - A module for generating image description and tags based on computer vision.
- [Wagtail FilePreviews](https://github.com/filepreviews/wagtail-filepreviews) - Extend Wagtail's Documents with image previews and metadata from FilePreviews.io.
- [Wagtail-Textract](https://github.com/fourdigits/wagtail_textract) - Make Wagtail search Documents contents (PDF, Excel and Word, etc.).
- [Wagtail-Lazyimages](https://github.com/ptrck/wagtail-lazyimages) - A plugin that generates tiny blurry placeholder images for lazy loading Wagtail images medium.com style.

### Translations

- [Wagtail Modeltranslation](https://github.com/infoportugal/wagtail-modeltranslation) - Simple app containing a mixin model that integrates [django-modeltranslation](https://github.com/deschler/django-modeltranslation) into Wagtail panels system.
- [wagtailtrans](https://github.com/LUKKIEN/wagtailtrans) - A Wagtail add-on for supporting multilingual sites.

### Forms

- [wagtailpolls](https://github.com/takeflight/wagtailpolls) - A plugin for adding polling capabilities to the Wagtail CMS.
- [Wagtailsurveys](https://github.com/torchbox/wagtailsurveys) - A module for Wagtail which provides the ability to build polls and surveys.
- [Wagtail ReCaptcha](https://github.com/springload/wagtail-django-recaptcha) - wagtail-django-captcha provides an easy way to integrate the [django-recaptcha](https://github.com/praekelt/django-recaptcha) field when using the Wagtail formbuilder.
- [wagtailstreamforms](https://github.com/AccentDesign/wagtailstreamforms) - Build forms in Wagtail's admin for use in streamfields.
- [wagtail-contact-reply](https://github.com/KalobTaulien/wagtail-contact-reply) - Reply directly to form submissions from the Wagtail admin

### Testing

- [wagtail-linkchecker](https://github.com/takeflight/wagtail-linkchecker) - A tool to assist with finding broken links on your Wagtail site.
- [Wagtail Accessibility](https://github.com/takeflight/wagtail-accessibility) – A plugin to assist with accessibility when developing in Wagtail.
- [Wagtail Factories](https://github.com/mvantellingen/wagtail-factories) - Factory boy classes for Wagtail.
- [Wagtail Foliage](https://github.com/harrislapiroff/wagtail-foliage) - Utilities for programmatically building page trees in Wagtail.

### Modeladmin

- [wagtail-admin-list-controls](https://github.com/ixc/wagtail-admin-list-controls) - Adds advanced search, ordering and layout controls to Wagtail's modeladmin list views.

### Misc

- [wagtailmenus](https://github.com/rkhleics/wagtailmenus) - An extension for Torchbox's Wagtail CMS to help you manage and render multi-level navigation and simple flat menus in a consistent, flexible way.
- [Wagtail Error Pages](https://gitlab.com/alexgleason/wagtailerrorpages) - Pretty, smart, customizable error pages for Wagtail.
- [Wagtail Themes](https://github.com/moorinteractive/wagtail-themes) - Site-specific theme loader for Wagtail.
- [Wagtail Sharing](https://github.com/cfpb/wagtail-sharing) – Easier sharing of Wagtail drafts.
- [Wagtail Gridder](https://github.com/wharton/wagtailgridder) - Grid card layout similar to Google image search results, with an expanded area for card details.
- [Wagtail Condensed Inline Panel](https://github.com/wagtail/wagtail-condensedinlinepanel) - Drop-in replacement for Wagtail's InlinePanel suited for large number of inlines (collapsible with drag and drop support).
- [Joyous](https://github.com/linuxsoftware/ls.joyous) - A calendar application for Wagtail.
- [Wagtail App Pages](https://github.com/mwesterhof/wagtail_app_pages) - Extend Wagtail pages using an actual URL config and django views.
- [Wagtail Import Export](https://github.com/torchbox/wagtail-import-export) - Import/Export pages between Wagtail instances.
- [Wagtail Import/Export Tool](https://github.com/berkalpyakici/wagtail-import-export-tool) - Refactor of [Wagtail Import Export](https://github.com/torchbox/wagtail-import-export). This tool supports importing/exporting images, documents, and snippets that are used on imported/exported pages.
- [Wagtail Tag Manager](https://github.com/jberghoef/wagtail-tag-manager) - A Wagtail addon that allows for easier and GDPR compliant administration of scripts and tags.
- [Wagtail Cache](https://github.com/coderedcorp/wagtail-cache) - A simple page cache for Wagtail using the Django cache middleware.
- [Wagtail GraphQL](https://github.com/tr11/wagtail-graphql) - App to automatically add GraphQL support to a Wagtail website.
- [Wagtail Orderable](https://github.com/elton2048/wagtail-orderable) - Mixin support for drag-and-drop ordering in admin panel.
- [Wagtail Live Preview](https://github.com/KalobTaulien/wagtail-livepreview) - Live page previews beside your content.
- [Wagtail Resume](https://github.com/adinhodovic/wagtail-resume) – A Wagtail project made to simplify creation of resumes for developers.

## Tools

- [Wagtail Cookiecutter Foundation](https://github.com/chrisdev/wagtail-cookiecutter-foundation) - A Cookiecutter template for Wagtail CMS using Zurb Foundation 6.
- [Beginner Wagtail Cookiecutter](https://github.com/heymonkeyriot/beginner-wagtail) – A super simple implementation of Wagtail CMS.
- [Wagtail Starter Kit](https://github.com/tkjone/starterkit-wagtail) – A cookiecutter complete with wagtail, django layout, vagrant, provisioning scrips, front end build system and more!
- [Wagtail Pipit](https://github.com/Frojd/Wagtail-Boilerplate) – Pipit is a Wagtail boilerplate which aims to provide an easy and modern developer workflow with a React-rendered frontend.
- [Django Cookiecutter Wagtail](https://github.com/Jean-Zombie/cookiecutter-django-wagtail) – A Django Cookiecutter template with Wagtail. Based on the original 'Django Cookiecutter'. Features: Docker support using `docker-compose` for development and production (using Traefik with LetsEncrypt support), customizable PostgreSQL version, Bootstrap 4, media storage using Amazon S3 or Google Cloud Storage and many more.

## Resources

### Getting started

- [Getting started in Wagtail, a newcomer's perspective](https://wagtail.io/blog/getting-started-wagtail-newcomers-perspective/) - Having used Drupal almost exclusively as my main tool of choice for a while now, I was asked to put together a build using Wagtail. By [@kiwimind](https://twitter.com/kiwimind).
- [Présentation de Wagtail, le dernier CMS Django](https://makina-corpus.com/blog/metier/2016/presentation-de-wagtail-le-dernier-cms-django) - Wagtail est un CMS relativement récent dans l’écosystème Django. Pour autant, son jeune âge ne l’empêche pas de posséder de nombreuses fonctionnalités que nous découvrirons dans cet article.
- [Getting Started With Wagtail](https://vix.digital/insights/getting-started-wagtail/) - Working extensively with Wagtail and the surrounding community, we have discovered a range of common pitfalls developers run into when beginning to deliver with Wagtail.

### Articles

- [Extending The Functionality of Email Forms in Wagtail](https://posts-by.lb.ee/dev-wagtail-extending-the-functionality-of-email-forms-232c8469ac97)
- [Wagtail: 2 Steps for Adding Pages Outside of the CMS](https://www.caktusgroup.com/blog/2016/02/15/wagtail-2-steps-adding-pages-outside-cms/)
- [Code blocks for Wagtail using Pygments](https://jordi.nz/code-blocks-wagtail-using-pygments/)
- [Adding document previews to Wagtail CMS](https://filepreviews.io/blog/2017/04/20/adding-document-previews-to-wagtail/)
- [Wagtail Tutorials: Build Blog Step by Step](https://www.accordbox.com/blog/wagtail-tutorials/) - The tutorials teach you how to create a standard blog from scratch step by step.
- [Python CMS Framework Review: Wagtail vs Django-CMS](https://www.accordbox.com/blog/python-cms-framework-review-wagtail-vs-django-cms/) - Talk about the difference between Django-CMS and Wagtail, the two most popular CMS framework in Python world.
- [Deploying Wagtail In Production](https://vix.digital/insights/deploying-wagtail-production/)
- [Setting Up Foundation Sass With Wagtail](https://vix.digital/insights/setting-foundation-sass-wagtail/)
- [Upgrading to Wagtail 2.0](https://wagtail.io/blog/upgrading-to-wagtail-2/) – Wagtail 2.0 is one of our biggest releases to date.
- [Getting started with Draftail extensions](https://thib.me/getting-started-with-draftail-extensions) – Do you want to write extensions for Draftail? This is a good place to start.
- [Amplify a Wagtail/Django site](https://parbhatpuri.com/amplify-wagtail-django-site-urls-part-1.html) - Prepare you Wagtail site for Accelerated Mobile Pages (AMP).
- [Migrating your Drupal content to Wagtail](https://medium.com/@kevinhowbrook/migrating-your-drupal-content-to-wagtail-d43bb34529e8)
- [How to Add Buttons to ModelAdmin Index View](https://timonweb.com/tutorials/how-to-add-buttons-to-modeladmin-index-view-in-wagtail-cms/)
- [How to Prevent Users from Creating Pages by Type](https://timonweb.com/tutorials/prevent-users-from-creating-certain-page-types-in-wagtail-cms/)
- [Drupal Front End WTF, Wagtail Front End FTW](https://medium.com/@kevinhowbrook/drupal-front-end-wtf-wagtail-front-end-ftw-17712628df3e) - Comparing Drupal and Wagtail Markup and approach to each CMS
- [How to Create and Manage Menus of Wagtail application](https://www.accordbox.com/blog/wagtail-tutorial-12-how-create-and-manage-menus-wagtail-application/)

### Recipes

- [Oscar Wagtail demo project](https://github.com/LUKKIEN/oscar-wagtail-demo) - A Django recipe for integrating Oscar E-commerce into a Wagtail CMS application.

### Presentations

- [An Introduction to Wagtail](https://www.youtube.com/watch?v=glIIF-kBXf0) by Eloise "Ducky" Macdonald-Meyer - This talk is an introduction to Wagtail, a content management system built on the Python web framework, Django.
- [DjangoCon US 2015 - Wagtail - Yet Another Django CMS](https://www.youtube.com/watch?v=6j0NVq6g4FE) by Tom Dyson - Tom will explain why his agency decided to build a new CMS, share some lessons learned in running a growing open source project, and outline Wagtail's roadmap to version 2 and beyond. [Slide deck](https://speakerdeck.com/tomdyson/wagtail-yet-another-cms-djangocon-us-2015).
- [Wellington Wagtail CMS Meetup - Meet Wagtail](https://docs.google.com/presentation/d/19EGWFtfHovHSAvyHCnLbxK50IAR2o7WwKd709cqi9p4/edit) by Josh, Jordi and Rich, from the Springload dev team - An introductory session to Wagtail to showcase the main features it has to offer.
- [DjangoCon US 2016 - Atomic Wagtail](https://www.youtube.com/watch?v=kqAKiouk1lY) by Kurt Wall – Brad Frost's atomic design principles are taking the way we design the web by storm. I'll explain what Wagtail is, how you can use it with atomic design principles, and some hurdles you might run into along the way with suggestions on how to help.
- [PyCon Australia – Comparing Wagtail, Django CMS and Mezzanine](https://www.youtube.com/watch?v=3UC1MNFOjEI) by Adam Brenecki – This talk explores the different approaches, strengths and weaknesses of each CMS, and what they mean for you as a developer and for your content editors.
- [Wagtail — еще одна CMS на Django](https://www.youtube.com/watch?v=yRmZ6WUfoOc) by Mikalai Radchuk - This talk is an introduction to Wagtail in Russian.
- [Wagtail & Agile – Wagtail Space 2017](https://youtu.be/-Qii_AyQsxE?t=2m21s) by Edd Baldry.
- [Deploy Wagtail to the Divio Cloud – Wagtail Space 2017](https://youtu.be/-Qii_AyQsxE?t=38m13s) by Daniele Procida.
- [All about Wagtail – Wagtail Space 2017](https://youtu.be/OedQi5W3Zho) by Robin van der Rijst.
- [Presenting Wagtail Clear StreamField, a modular StreamField app – Wagtail Space 2017](https://youtu.be/OedQi5W3Zho?t=19m1s) by Edd Baldry.
- [Wagtail Experiments, easy A/B testing for your Wagtail sites – Wagtail Space 2017](https://youtu.be/OedQi5W3Zho?t=34m37s) by Tom Dyson.
- [Wagtail's preview, a new hope – Wagtail Space 2017](https://www.youtube.com/watch?v=ObM2pUgY-bs) by Bertrand Bordage.
- [The Zen of Wagtail – Wagtail Space 2017](https://youtu.be/ObM2pUgY-bs?t=16m38s) by Matt Westcott.
- [Plone to Wagtail – Wagtail Space 2017](https://youtu.be/hZcuq8WJVew?t=2m57s) by Coen van der Kamp.
- [Hundreds of Wagtail in Flight – Wagtail Space 2017](https://youtu.be/hZcuq8WJVew?t=24m9s) by Simon de Haan.
- [How Google uses Wagtail – Wagtail Space 2018](https://www.youtube.com/watch?v=lh9nmN1mzwQ&t=1937s) by Kevin Chung.
- [Introducing Draft.js in Wagtail – Wagtail Space 2018](https://www.youtube.com/watch?v=lh9nmN1mzwQ&t=2690s) by Thibaud Colas. [Presentation](https://thib.me/introducing-draft-js-in-wagtail).
- [Let It Go – Wagtail Space 2018](https://www.youtube.com/watch?v=lh9nmN1mzwQ&t=3938s) by Matt Wescott.
- [Developing Solutions for Girls, by Men – Wagtail Space 2018](https://www.youtube.com/watch?v=lh9nmN1mzwQ&t=5184s) by Lisa Adams.
- [Wagtail’s first hatch – Wagtail Space 2018](https://www.youtube.com/watch?v=P8RUQE7Djdg&t=265s) by Bertrand Bordage.
- [The Word Problem – Wagtail Space 2018](https://www.youtube.com/watch?v=P8RUQE7Djdg&t=2841s) by Tom Dyson.
- [Wagtail on Divio Cloud – Wagtail Space 2018](https://www.youtube.com/watch?v=P8RUQE7Djdg&t=3856s) by Daniele Procida.
- [Chopping the head off Wagtail and sticking it back on – Wagtail Space 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=152s) by Tony Yates.
- [StreamField editor at UWKM – Wagtail Space 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=400s) by Geert jan Hoogeslag.
- [Things i learned at Wagtail Space – Wagtail Space 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=719s) by Codie Roelf.
- [Fly Wagtail to a PyCon – Wagtail Space 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=912s) by Daniele Procida.
- [Wagtail Performance – Wagtail Space 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=1345s) by Michael van Tellingen. [Code](https://gist.github.com/mvantellingen/daebda6abbaa9a5ed0888f886a77fcf0).
- [Mutliple images uploader – Wagtail Space 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=1661s) by Rajeev J Sebastian.
- [Wagtail Space easter egg team demo – Wagtail Space 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=2057s) by Lars. [Code](https://github.com/specialunderwear/haunted-wagtail).
- [Wagtail Space 2019 – Wagtail Space 2018](https://www.youtube.com/watch?v=u0CPaXRSOzI&t=2278s) by Maarten Kling.
- [Wagtail in 2018 – Wagtail Space US 2018](https://www.youtube.com/watch?v=ICKYMO0YoFI&index=2&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV) by Tom Dyson.
- [What the Wagtail Docs Don't Tell You – Wagtail Space US 2018](https://www.youtube.com/watch?v=PCkxBNXWM64&index=3&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV) by Lacey Williams Henschel.
- [Django Logging for Wagtail – Wagtail Space US 2018](https://www.youtube.com/watch?v=kkztl9ORUKQ&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV&index=4) by Ryan Sullivan.
- [Scaling Wagtail for 100 Million Girls – Wagtail Space US 2018](https://www.youtube.com/watch?v=AiOJAKE0M0I&index=5&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV) by Lisa Adams and Codie Roelf.
- [Using Wagtail to Fight for Press Freedom – Wagtail Space US 2018](https://www.youtube.com/watch?v=FYqbqsa04T8&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV&index=6) by Harris Lapiroff.
- [Choosing Wagtail for Columbia University – Wagtail Space US 2018](https://www.youtube.com/watch?v=OiZScRcluCo&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV&index=7) by Zarina Mustapha.
- [Running a Multi-Site Newsroom in Wagtail – Wagtail Space US 2018](https://www.youtube.com/watch?v=lMCjInjAz-M&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV&index=8) by Ryan Verner.
- [Wagtail in the Cloud – Wagtail Space US 2018](https://www.youtube.com/watch?v=N1MeTEPRmJA&index=9&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV) by Daniele Procida.
- [Beheading Wagtail: Wagtail as a Headless CMS – Wagtail Space US 2018](https://www.youtube.com/watch?v=HZT14u6WwdY&index=10&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV) by Michael Harrison.
- [Learning Wagtail – Wagtail Space US 2018](https://www.youtube.com/watch?v=C-tXt5fLj_s&index=11&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV) by Dawn Wages.
- [Sharing is Caring – Wagtail Space US 2018](https://www.youtube.com/watch?v=6AXyg6vvMTE&index=12&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV) by Andy Chosak.
- [Lightning Talks – Wagtail Space US 2018](https://www.youtube.com/watch?v=uoxyBIpaXTU&index=13&list=PLEyaio0l1qoGGbXg3XH0205FIF32oO1wV)
- [Wagtail: когда хочется чего-то приятнее, чем просто Django – Moscow Python Conf++ 2018](https://www.youtube.com/watch?v=xPPfTvLS7oQ) by Игорь Мосягин
- [The State of Wagtail – Wagtail Space 2019](https://youtu.be/MAzZ2lhMhzM?t=592) by Tom Dyson.
- [Image rotation feature – Wagtail Space 2019](https://youtu.be/MAzZ2lhMhzM?t=2057) by Chris Adams. Code.
- [Debug templates – Wagtail Space 2019](https://youtu.be/MAzZ2lhMhzM?t=2264) by Coen van der Kamp.
- [Wagtail Headless with HATEOAS – Wagtail Space 2019](https://youtu.be/MAzZ2lhMhzM?t=2567) by Duco Dokter.
- [Building a Planet Friendly Web (with Wagtail) – Wagtail Space 2019](https://youtu.be/MAzZ2lhMhzM?t=2926) by Chris Adams.
- [[WIP] The future of (rich text) authoring experiences in Wagtail – Wagtail Space 2019](https://youtu.be/MAzZ2lhMhzM?t=4067) by Thibaud Colas.
- [Wagtail & Whatsapp – Wagtail Space 2019](https://youtu.be/CSwpj-jyjP4?t=47) by Lisa Adams & Codie Roelf.
- [Slack2Wagtail – Wagtail Space 2019](https://youtu.be/CSwpj-jyjP4?t=785) by Coen van der Kamp & Lucas Moeskops.
- [Wagtail and Oscar – Wagtail Space 2019](https://youtu.be/CSwpj-jyjP4?t=1634) by Lars van de Kerkhof.
- [wagtail-textract – Wagtail Space 2019](https://youtu.be/CSwpj-jyjP4?t=3313) by Kees Hink. [Code](https://github.com/fourdigits/wagtail_textract).
- [Django 2.2 compatibility – Wagtail Space 2019](https://youtu.be/CSwpj-jyjP4?t=3468) by Matt Wescott.
- [SEO dashboard – Wagtail Space 2019](https://youtu.be/CSwpj-jyjP4?t=3937) by Janneke Janssen. [Code](https://github.com/LUKKIEN/wagtail-marketing-addons).
- [My First Wagtail Contribution – More formats in RichText Editor – Wagtail Space 2019](https://youtu.be/CSwpj-jyjP4?t=4126) by Arifin Ibne Matin.
- [Fly, Wagtail, fly! – Wagtail Space 2019](https://youtu.be/CSwpj-jyjP4?t=4404) by Daniele Procida.
- [Wagtail & GraphQL – Wagtail Space 2019](https://youtu.be/YydSbL8gMS4?t=24) by Arthur Bayr.
- [Writing (code) for authors – Wagtail Space US 2019](https://www.youtube.com/watch?v=Ihsrki0d1G8&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=1) by Brian Smith & Eric Sherman. [Slides](https://docs.google.com/presentation/d/1z61u0uKwJxmYS4Zawbu4Zgg-kCtInd1VgsEg-rnwzBE/edit).
- [Saving Lives With Wagtail: Recovery Meetings Across the World – Wagtail Space US 2019](https://www.youtube.com/watch?v=QlLWvNT5Wrk&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=2) by Timothy Allen.
- [Why we chose Wagtail for CodeRed CMS – Wagtail Space US 2019](https://www.youtube.com/watch?v=1JUOAAmLQFA&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=3) by Vince Salvino.
- [Building a Wagtail-based site and authoring environment with accessibility in mind – Wagtail Space US 2019](https://www.youtube.com/watch?v=CxjlAI6R7iY&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=4) by Zarina Mustapha.
- [Making Wagtail Accessible – Wagtail Space US 2019](https://www.youtube.com/watch?v=tdB1I_gSCeY&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=5) by Thibaud Colas. [Slides](https://docs.google.com/presentation/d/15y8XIe7SL-RYEO9tEE8n9chx80_X4j4PbczGGM-cEGE/edit).
- [Everyone can fly a flag – Wagtail Space US 2019](https://www.youtube.com/watch?v=ZqwmgsqMTEs&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=6) by Will Barton. [Slides](https://docs.google.com/presentation/d/1-A1doke2ylcqG72oIP-MLiX8SKXKkKNxQeKxddYUGBw/edit).
- [Architecting for a multi-domain site – Wagtail Space US 2019](https://www.youtube.com/watch?v=xMbJmHF7kCw&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=7) by Ben Beecher. [Slides](https://slides.com/benbeecher/mds/).
- [Contributions can be more than code – Wagtail Space US 2019](https://www.youtube.com/watch?v=tK-3kEBbblg&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=8) by Kalob Taulien.
- [Thoughtful Code Review – Wagtail Space US 2019](https://www.youtube.com/watch?v=RY0K1BEV-_U&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=9) by Naomi Morduch Toubman. [Slides](https://docs.google.com/presentation/d/1b_Hda8381G6mMc7uzYDc2EYjocfwSi2TYiRMI7d4e3I/).
- [Solving your problems by spelunking the Wagtail code – Wagtail Space US 2019](https://www.youtube.com/watch?v=BMoOhjgirFM&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=10) by Harris Lapiroff. [Slides](https://harrislapiroff.github.io/wagtail-space-us-2019/)
- [The State of Wagtail: 2019 – Wagtail Space US 2019](https://www.youtube.com/watch?v=s29vaGnFcq8&list=PLEyaio0l1qoEIUFM9bnRKoN6VKEUOdxAn&index=11) by Tom Dyson.

### Podcasts

- [Podcast.__init__ Episode 58 - Wagtail with Tom Dyson](https://www.podcastinit.com/episode-58-wagtail-with-tom-dyson/) - In this episode Tom Dyson explains how Wagtail came to be created, what sets it apart from other options, and when you should implement it for your projects.
- [Django Chat: Wagtail CMS - Tom Dyson](https://django-chat.simplecast.com/episodes/wagtail-cms-tom-dyson) - An interview with Tom Dyson on Wagtail, the leading Django-based CMS used by tens of thousands of organizations including Google, NASA, and the British NHS.

### Videos

- [Learn Wagtail](https://learnwagtail.com/) - Regular video tutorials about all aspects of Wagtail.
- [Wagtail screencasts: Creating and displaying pages in Wagtail](https://www.youtube.com/watch?v=o_dFgr8HZYU) - This video will show you how to create and display pages using the Wagtail CMS.
- [Draftail extensions – custom entities tutorial](https://www.youtube.com/watch?v=nCMgoTerEb4) - Step-by-step tutorial to make extensions for Draftail.
- [Wagtail Wednesdays #01 - Adding Help Text to Improve Wagtail Editor Experience](https://www.youtube.com/watch?v=ciYNMcv3lE0) - Catherine talks you through the steps you can take to add some useful supplementary text fields to the Wagtail admin.
- [Wagtail Wednesdays #02 - Customising Rich Text Features in Wagtail](https://www.youtube.com/watch?v=ei7ot_Wry3o) - Catherine talks you through the steps you can take to customise your rich text editors to control which features are available to your content editors.
- [Wagtail Wednesdays #03 - Using tabs to create a cleaner admin interface](https://www.youtube.com/watch?v=uZc0aZrHtQw) - Chris talks you through using tabs to organise fields.
- [Wagtail Wednesdays #04 - Organising Images and Documents using Wagtail Collections](https://www.youtube.com/watch?v=HGXHtFpLDCA) - Kieran talks you through the process of organising your images and documents into collections.
- [Wagtail Wednesdays #05 - How to organise your fields and streamline the editor experience](https://www.youtube.com/watch?v=CedcZmQ9KHs) - Chelsea talks you through the process of organising your fields to make it easier to manage them and streamline the editor experience.
- [Wagtail Wednesdays #06 - Creating & using custom settings in your wagtail site](https://www.youtube.com/watch?v=KJWCGq3IRNc) - Chris talks you through setting up and using custom site settings.
- [Wagtail Wednesdays #07 - How to Enable the Wagtail Styleguide](https://www.youtube.com/watch?v=_CfU9UivYPI) - It’s a really helpful resource that takes no time at all to enable and it allows you to check your components against the guidelines and shows all the available Wagtail icons.
- [How to Deploy Wagtail to Google App Engine](https://www.youtube.com/watch?v=uD9PTag2-PQ) - Focus is Google Cloud Platform but a great introduction on how to get Wagtail up and running in their PAAS.

### Showcases

- [Made with Wagtail](https://madewithwagtail.org/) - A showcase of sites and apps made with Wagtail CMS.
- [Contributed apps and website code](https://github.com/torchbox/wagtail/wiki/Contributed-apps-and-website-code) - A provisional directory of third-party contributed Wagtail websites and apps.

### Lists

- [PyPI - Python Package Index](https://pypi.org/search/?q=Wagtail) - Wagtail packages on the Python Package Index.
- [Django Packages](https://djangopackages.org/grids/g/wagtail-cms/) - Wagtail projects and packages on Django Packages.

## For editors

- [How Do I Wagtail?](https://foundation.mozilla.org/en/docs/how-do-i-wagtail/) - Mozilla's editor facing guide for how to use Wagtail's admin interface. Source for this hosted on [Mozilla's Github](https://github.com/mozilla/foundation.mozilla.org/tree/master/network-api/networkapi/wagtailpages)

## Community

- [Dutch Wagtail Meetup](https://www.meetup.com/Dutch-Wagtail-Meetup/) - This is a group for anyone interested in working and developing with Wagtail.
- [Wellington Wagtail CMS Meetup](https://www.meetup.com/Wellington-Wagtail-CMS-Meetup/) - The first Wagtail CMS meetup in New Zealand!
- [Wagtail Space](https://www.wagtail.space/) - Wagtail training sessions, Wagtail (lightning) talks and a Wagtail sprint. From March 13th until 15th 2019, Wagtail Space takes place in Arnhem, The Netherlands.
- [Wagtail’s first hatch](https://www.kickstarter.com/projects/noripyt/wagtails-first-hatch) – Kickstarter campaign to accelerate the development of Wagtail.

## Open-source sites

- [bakerydemo](https://github.com/wagtail/bakerydemo) – Next generation Wagtail demo, born in Reykjavík.
- [wagtaildemo](https://github.com/wagtail/wagtaildemo) – An example site implemented with Wagtail.
- [Torchbox](https://github.com/torchbox/wagtail-torchbox) – Wagtail build of Torchbox.com.
- [Made with Wagtail](https://github.com/springload/madewithwagtail) - A showcase of sites and apps made with Wagtail CMS.
- [OpenCanada.org](https://github.com/OpenCanada/website) – The opencanada.org website source.
- [Federal Electoral Commission](https://github.com/18F/fec-cms) – The content management system (CMS) for the new Federal Election Commission website.
- [Table Tennis Wellington Business Class](https://github.com/jordij/bctt.nz) – Website for the table tennis business league in Wellington NZ.
- [Jordi Joan’s blog](https://github.com/jordij/jordijoan.me) – Personal blog site using Wagtail CMS.
- [Localore: Finding America](https://github.com/ghostwords/localore) – Wagtail-based CMS and Ansible playbooks for Localore: Finding America.
- [Adventure Capitalists](https://github.com/AdventureCapitalists/website) – Wagtail powered website for the world's only investment band.
- [NHS.UK Content Store](https://github.com/nhsuk/nhsuk-content-store) – NHS.UK content store and editing app.
- [dev.hel.fi](https://github.com/City-of-Helsinki/devheldev) – City of Helsinki development site with Wagtail.
- [Digital Helsinki](https://github.com/City-of-Helsinki/digihel) – City of Helsinki Digital Helsinki Wagtail CMS.
- [Secure the News](https://github.com/freedomofpress/securethenews) – An automated scanner and web dashboard for tracking TLS deployment across news organizations.
- [HackSoft](https://github.com/HackSoftware/hacksoft.io) – Website for HackSoft.
- [HackConf](https://github.com/HackSoftware/hackconf.bg) – Website for the annual HackConf.
- [RTEI](https://github.com/okfn/rtei) – Right to Education Index website (OKFN).
- [BVSPCA](https://github.com/nfletton/bvspca) – Bow Valley SPCA website.
- [Project TIER](https://github.com/ProjectTIER/projecttier.org) – Teaching Integrity in Empirical Research.
- [SecureDrop](https://github.com/freedomofpress/securedrop.org) – Wagtail-powered website of the SecureDrop whistleblower document submission system.
- [Consumer Financial Protection Bureau](https://github.com/cfpb/cfgov-refresh) – The source code of the Wagtail-powered consumerfinance.gov is available here on GitHub.

## Contribute

Contributions are always welcome!
Please read the [contribution guidelines](.github/CONTRIBUTING.md) first.

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Springload](https://www.springload.co.nz/) has waived all copyright and related or neighboring rights to this work.
