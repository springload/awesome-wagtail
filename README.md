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
  - [Streamfield](#streamfield)
  - [Static site generation](#static-site-generation)
  - [Settings management](#settings-management)
  - [E-commerce](#e-commerce)
  - [SEO and SMO](#seo-and-smo)
  - [Analytics](#analytics)
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
- [Community](#community)
  - [Meetups](#meetups)
- [Open-source sites](#open-source-sites)

## General resources

- [Official site](https://wagtail.io/)
- [GitHub repository](https://github.com/wagtail/wagtail)
- [Twitter account](https://twitter.com/wagtailcms)
- [Roadmap](https://github.com/wagtail/wagtail/projects/1)

## Apps

### Blogging/news

- [Puput](http://puput.readthedocs.org/) - Puput is a powerful and simple Django app to manage a blog. It uses the awesome Wagtail CMS as content management system.
- [wagtail_blog](https://github.com/thelabnyc/wagtail_blog) - A WordPress-like blog app implemented in Wagtail.
- [wagtailnews](https://github.com/takeflight/wagtailnews) - A plugin for Wagtail that provides news / blogging functionality.
- [wagtail-blog-app](https://github.com/Tivix/wagtail-blog-app) - A blog application for the Wagtail Django CMS.
- [Django Wagtail Feeds](https://github.com/chrisdev/django-wagtail-feeds) - Add support for RSS Feeds, Facebook Instant Articles and Apple News Publisher to your Wagtail CMS Projects.

### Rich text editor extensions

- [wagtail-readability](https://github.com/takeflight/wagtail-readability) - Test how readable the content you enter into Wagtail is.
- [wagtailembedder](https://github.com/springload/wagtailembedder) - Snippets embedder for Wagtail richtext fields.
- [Wagtail TinyMCE](https://github.com/isotoma/wagtailtinymce) - A TinyMCE editor integration for Wagtail.
- [Wagtail Froala](https://github.com/jaydensmith/wagtailfroala) - Extends Wagtail to use the Froala WYSIWYG editor in RichTextField/RichTextBlock.

### Widgets

- [wagtailgmaps](https://github.com/springload/wagtailgmaps) - Simple Google Maps address formatter for Wagtail fields.
- [Wagtail-Geo-Widget](https://github.com/Frojd/wagtail-geo-widget) - Google Maps widget for the GeoDjango PointField field in Wagtail.
- [wagtail-markdown](https://github.com/torchbox/wagtail-markdown) - Markdown fields and blocks for Wagtail.

### Streamfield

- [Wagtail FontAwesome](https://github.com/alexgleason/wagtailfontawesome) - Add FontAwesome icons to StreamField.
- [Wagtail Commonblocks](https://github.com/springload/wagtailblocks) - Common StreamField blocks for Wagtail.
- [Wagtail SVGmap](https://github.com/City-of-Helsinki/wagtail-svgmap) - ImageMap functionality for Wagtail through inline SVGs.
- [Wagtail ClearStream](https://github.com/heymonkeyriot/wagtailclearstream) - An app to make Wagtail's StreamField more modular.
- [UWKM Streamfields](https://github.com/UWKM/uwkm_streamfields) – A basic set of Wagtail Streamfields for fun and profit.

### Static site generation

- [Wagtail-bakery](https://github.com/moorinteractive/wagtail-bakery) - A set of helpers for baking your Django Wagtail site out as flat files.

### Settings management

- [Wagtail-Constance](https://github.com/MechanisM/wagtail-constance) - django-constance integration for Wagtail CMS.
- [Wagtail-Flags](https://github.com/cfpb/wagtail-flags) - Feature flags for Wagtail sites.

### E-commerce

- [wagtailinvoices](https://github.com/SableWalnut/wagtailinvoices) - A Wagtail module for creating invoices.
- [wagtail-saleor](https://github.com/mirumee/wagtail-saleor) - An e-commerce application based on Wagtail and Satchless.
- [longclaw](https://github.com/JamesRamm/longclaw) - A shop template for Wagtail CMS.
- [django-oscar-wagtail](https://github.com/LabD/django-oscar-wagtail) - Wagtail integration for Oscar Commerce (or Oscar Commerce integration for Wagtail?)

### SEO and SMO

- [wagtail-metadata](https://github.com/takeflight/wagtail-metadata) - A tool to assist with metadata for social media and search engines.
- [wagtail-metadata-mixin](https://github.com/bashu/wagtail-metadata-mixin) - OpenGraph, Twitter Card and Google+ snippet tags for Wagtail CMS pages.
- [wagtail-schema.org](https://github.com/takeflight/wagtail-schema.org) - Schema.org JSON-LD tags for Wagtail sites.

### Analytics

- [Wagtail Analytics](https://github.com/tomdyson/wagalytics) - A Google Analytics dashboard in your Wagtail admin.
- [Wagtail Experiments](https://github.com/torchbox/wagtail-experiments) – A/B testing for Wagtail.

### Security

- [wagtailenforcer](https://github.com/springload/wagtailenforcer) - If you need to enforce security protocols on your Wagtail site you've come to the right place.
- [wagtail-yubikey](https://github.com/ahopkins/wagtail-yubikey) - Enable YubiKey two factor authentication on Wagtail admin panel.

### Media

- [wagtailmedia](https://github.com/torchbox/wagtailmedia) - A Wagtail module for managing video and audio files within the admin.
- [wagtail-embedvideos](https://github.com/infoportugal/wagtail-embedvideos) - Simple app that works similar to wagtailimages, but for embedding YouTube and Vimeo videos and music from SoundCloud. It's an integration of [django-embed-video](https://github.com/yetty/django-embed-video).
- [Wagtail Alt Generator](https://github.com/marteinn/wagtail-alt-generator) - A module for generating image description and tags based on computer vision.
- [Wagtail FilePreviews](https://github.com/filepreviews/wagtail-filepreviews) - Extend Wagtail's Documents with image previews and metadata from FilePreviews.io.

### Translations

- [Wagtail Modeltranslation](https://github.com/infoportugal/wagtail-modeltranslation) - Simple app containing a mixin model that integrates [django-modeltranslation](https://github.com/deschler/django-modeltranslation) into Wagtail panels system.
- [wagtailtrans](https://github.com/LUKKIEN/wagtailtrans) - A Wagtail add-on for supporting multilingual sites.

### Forms

- [wagtailpolls](https://github.com/takeflight/wagtailpolls) - A plugin for adding polling capabilities to the Wagtail CMS.
- [Wagtailsurveys](https://github.com/torchbox/wagtailsurveys) - A module for Wagtail which provides the ability to build polls and surveys.
- [Wagtail ReCaptcha](https://github.com/springload/wagtail-django-recaptcha) - wagtail-django-captcha provides an easy way to integrate the [django-recaptcha](https://github.com/praekelt/django-recaptcha) field when using the Wagtail formbuilder.

### Testing

- [wagtail-linkchecker](https://github.com/takeflight/wagtail-linkchecker) - A tool to assist with finding broken links on your Wagtail site.
- [Wagtail Accessibility](https://github.com/takeflight/wagtail-accessibility) – A plugin to assist with accessibility when developing in Wagtail.
- [Wagtail Factories](https://github.com/mvantellingen/wagtail-factories) - Factory boy classes for Wagtail.

### Misc

- [Wagtail Plus](https://github.com/rfosterslo/wagtailplus) - Modular add-ons for Wagtail CMS.
- [wagtailmenus](https://github.com/rkhleics/wagtailmenus) - An extension for Torchbox's Wagtail CMS to help you manage and render multi-level navigation and simple flat menus in a consistent, flexible way.
- [Wagtail Error Pages](https://github.com/alexgleason/wagtailerrorpages) - Pretty, smart, customizable error pages for Wagtail.
- [Wagtail Themes](https://github.com/moorinteractive/wagtail-themes) - Site-specific theme loader for Wagtail.
- [Wagtail Sharing](https://github.com/cfpb/wagtail-sharing) – Easier sharing of Wagtail drafts.
- [Wagtail Postgres Search Backend](https://github.com/leukeleu/wagtail-pg-search-backend) - PostgreSQL full text search backend for Wagtail CMS.
- [Wagtail Gridder](https://github.com/wharton/wagtailgridder) - Grid card layout similar to Google image search results, with an expanded area for card details.

## Tools

- [Wagtail Cookiecutter Foundation](https://github.com/chrisdev/wagtail-cookiecutter-foundation) - A Cookiecutter template for Wagtail CMS using Zurb Foundation 6.
- [Beginner Wagtail Cookiecutter](https://github.com/heymonkeyriot/beginner-wagtail) – A super simple implementation of Wagtail CMS.
- [Wagtail Starter Kit](https://github.com/tkjone/starterkit-wagtail) – A cookiecutter complete with wagtail, django layout, vagrant, provisioning scrips, front end build system and more!

## Resources

### Getting started

- [Introducing Wagtail
](https://www.springload.co.nz/blog/introducing-wagtail/) - During the last few months we have spent a good amount of time working with Wagtail, a really cool CMS built on top of the well-known Django framework.
- [Getting started in Wagtail, a newcomer's perspective
](https://wagtail.io/blog/getting-started-wagtail-newcomers-perspective/) - Having used Drupal almost exclusively as my main tool of choice for a while now, I was asked to put together a build using Wagtail. By [@kiwimind](https://twitter.com/kiwimind).
- [Présentation de Wagtail, le dernier CMS Django
](http://makina-corpus.com/blog/metier/2016/presentation-de-wagtail-le-dernier-cms-django) - Wagtail est un CMS relativement récent dans l’écosystème Django. Pour autant, son jeune âge ne l’empêche pas de posséder de nombreuses fonctionnalités que nous découvrirons dans cet article.

### Articles

- [Interactive 360 degree product views as a Wagtail streamfield block](http://www.djangopaths.com/interactive-360-degree-product-views-wagtail-streamfield-block/)
- [Extending The Functionality of Email Forms in Wagtail](https://posts-by.lb.ee/dev-wagtail-extending-the-functionality-of-email-forms-232c8469ac97)
- [Wagtail: 2 Steps for Adding Pages Outside of the CMS](https://www.caktusgroup.com/blog/2016/02/15/wagtail-2-steps-adding-pages-outside-cms/)
- [Code blocks for Wagtail using Pygments](https://jordijoan.me/code-blocks-wagtail-using-pygments/)
- [Adding document previews to Wagtail CMS](http://filepreviews.io/blog/2017/04/20/adding-document-previews-to-wagtail/)

### Recipes

- [Oscar Wagtail demo project](https://github.com/LUKKIEN/oscar-wagtail-demo) - A Django recipe for integrating Oscar E-commerce into a Wagtail CMS application.

### Presentations

- [An Introduction to Wagtail](https://www.youtube.com/watch?v=glIIF-kBXf0) by Eloise "Ducky" Macdonald-Meyer - This talk is an introduction to Wagtail, a content management system built on the Python web framework, Django.
- [DjangoCon US 2015 - Wagtail - Yet Another Django CMS](https://www.youtube.com/watch?v=6j0NVq6g4FE) by Tom Dyson - Tom will explain why his agency decided to build a new CMS, share some lessons learned in running a growing open source project, and outline Wagtail's roadmap to version 2 and beyond. [Slide deck](https://speakerdeck.com/tomdyson/wagtail-yet-another-cms-djangocon-us-2015).
- [Wellington Wagtail CMS Meetup - Meet Wagtail](https://docs.google.com/presentation/d/19EGWFtfHovHSAvyHCnLbxK50IAR2o7WwKd709cqi9p4/edit) by Josh, Jordi and Rich, from the Springload dev team - An introductory session to Wagtail to showcase the main features it has to offer.
- [DjangoCon US 2016 - Atomic Wagtail](https://www.youtube.com/watch?v=kqAKiouk1lY) by Kurt Wall – Brad Frost's atomic design principles are taking the way we design the web by storm. I'll explain what Wagtail is, how you can use it with atomic design principles, and some hurdles you might run into along the way with suggestions on how to help.
- [PyCon Australia – Comparing Wagtail, Django CMS and Mezzanine](https://www.youtube.com/watch?v=3UC1MNFOjEI) by Adam Brenecki – This talk explores the different approaches, strengths and weaknesses of each CMS, and what they mean for you as a developer and for your content editors.

### Podcasts

- [Podcast.__init__ Episode 58 - Wagtail with Tom Dyson](http://podcastinit.com/tom-dyson-wagtail.html) - In this episode Tom Dyson explains how Wagtail came to be created, what sets it apart from other options, and when you should implement it for your projects.

### Videos

- [Wagtail screencasts: Creating and displaying pages in Wagtail
](https://www.youtube.com/watch?v=o_dFgr8HZYU) - This video will show you how to create and display pages using the Wagtail CMS.

### Showcases

- [Made with Wagtail](http://madewithwagtail.org/) - A showcase of sites and apps made with Wagtail CMS.
- [Contributed apps and website code](https://github.com/torchbox/wagtail/wiki/Contributed-apps-and-website-code) - A provisional directory of third-party contributed Wagtail websites and apps.

## Community

- [Wagtail Space](http://www.wagtail.space/) - Wagtail training sessions, Wagtail (lightning) talks and a Wagtail sprint. From March 21st until 25th, Wagtail Space takes place in Arnhem, The Netherlands.

### Meetups

- [Bristol Wagtail Users and Developers](https://www.meetup.com/Bristol-Wagtail-Users-and-Developers/) - The South West group (nest?) of people who work with Wagtail CMS.
- [Dutch Wagtail Meetup](http://www.meetup.com/Dutch-Wagtail-Meetup/) - This is a group for anyone interested in working and developing with Wagtail.
- [Wellington Wagtail CMS Meetup](http://www.meetup.com/Wellington-Wagtail-CMS-Meetup/) - The first Wagtail CMS meetup in New Zealand!

## Open-source sites

- [wagtaildemo](https://github.com/torchbox/wagtaildemo) – An example site implemented with Wagtail.
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

## Contribute

Contributions are always welcome!
Please read the [contribution guidelines](CONTRIBUTING.md) first.

## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Springload](https://www.springload.co.nz/) has waived all copyright and related or neighboring rights to this work.
