Awesome Wagtail [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) [![Build Status](https://travis-ci.org/springload/awesome-wagtail.svg?branch=master)](https://travis-ci.org/springload/awesome-wagtail) [<img src="https://github.com/torchbox/wagtail/blob/82171f70faaf0c8b8da278261e6f45fed529c899/docs/logo.png" width="83" align="right" alt="Wagtail">](https://wagtail.io/)
===============

> A curated list of awesome packages, articles, and other cool resources from the Wagtail community.

*You might also like [awesome-django](https://gitlab.com/rosarior/awesome-django) and [awesome-python](https://github.com/vinta/awesome-python). :snake:*

## Table of Contents

- [General resources](#general-resources)
- [Apps](#apps)
  - [Blogging/news](#bloggingnews)
  - [Rich text editor extensions](#rich-text-editor-extensions)
  - [Streamfield](#streamfield)
  - [Static site generation](#static-site-generation)
  - [Settings management](#settings-management)
  - [E-commerce](#e-commerce)
  - [Security](#security)
  - [Media](#media)
  - [Translations](#translations)
  - [Forms](#forms)
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

## General resources

- [Official site](https://wagtail.io/)
- [GitHub repository](https://github.com/torchbox/wagtail)
- [Twitter account](https://twitter.com/wagtailcms)
- [Roadmap](https://github.com/torchbox/wagtail/wiki/Roadmap)
- [Wagtail core meeting notes](https://github.com/torchbox/wagtail/wiki/Wagtail-core-meeting-notes), [Wagtail Core Meeting Notes](https://github.com/springload/wagtail-core-notes)

## Apps

### Blogging/news

- [Puput](http://puput.readthedocs.org/) - Puput is a powerful and simple Django app to manage a blog. It uses the awesome Wagtail CMS as content management system.
- [wagtail_blog](https://github.com/thelabnyc/wagtail_blog) - A WordPress-like blog app implemented in Wagtail.
- [wagtailnews](https://bitbucket.org/takeflight/wagtailnews) - A plugin for Wagtail that provides news / blogging functionality.
- [wagtail-blog-app](https://github.com/Tivix/wagtail-blog-app) - A blog application for the Wagtail Django CMS.

### Rich text editor extensions

- [wagtail-readability](https://github.com/takeflight/wagtail-readability) - Test how readable the content you enter into Wagtail is.
- [wagtailembedder](https://github.com/springload/wagtailembedder) - Snippets embedder for Wagtail richtext fields.
- [wagtailgmaps](https://github.com/springload/wagtailgmaps) - Simple Google Maps address formatter for Wagtail fields.
- [Wagtail TinyMCE](https://github.com/isotoma/wagtailtinymce) - A TinyMCE editor integration for Wagtail.
- [Wagtail Froala](https://github.com/jaydensmith/wagtailfroala) - Extends Wagtail to use the Froala WYSIWYG editor in RichTextField/RichTextBlock.

### Streamfield

- [wagtail-markdown](https://github.com/torchbox/wagtail-markdown) - Markdown fields and blocks for Wagtail.
- [Wagtail FontAwesome](https://github.com/alexgleason/wagtailfontawesome) - Add FontAwesome icons to StreamField.
- [Wagtail Commonblocks](https://github.com/springload/wagtailblocks) - Common StreamField blocks for Wagtail.

### Static site generation

- [Wagtail Bakery](https://github.com/mhnbcu/wagtailbakery) - SAMPLE module for Wagtail CMS static generation with Django Bakery.

### Settings management

- [Wagtail-Constance](https://github.com/MechanisM/wagtail-constance) - django-constance integration for Wagtail CMS.

### E-commerce

- [wagtailinvoices](https://github.com/SableWalnut/wagtailinvoices) - A Wagtail module for creating invoices.
- [wagtail-saleor](https://github.com/mirumee/wagtail-saleor) - An e-commerce application based on Wagtail and Satchless.

### Security

- [wagtailenforcer](https://github.com/springload/wagtailenforcer) - If you need to enforce security protocols on your Wagtail site you've come to the right place.
- [wagtail-yubikey](https://github.com/ahopkins/wagtail-yubikey) - Enable YubiKey two factor authentication on Wagtail admin panel.

### Media

- [wagtailmedia](https://github.com/torchbox/wagtailmedia) - A Wagtail module for managing video and audio files within the admin.
- [wagtail-embedvideos](https://github.com/infoportugal/wagtail-embedvideos) - Simple app that works similar to wagtailimages, but for embedding YouTube and Vimeo videos and music from SoundCloud. It's an integration of [django-embed-video](https://github.com/yetty/django-embed-video).

### Translations

- [Wagtail Modeltranslation](https://github.com/infoportugal/wagtail-modeltranslation) - Simple app containing a mixin model that integrates [django-modeltranslation](https://github.com/deschler/django-modeltranslation) into Wagtail panels system.

### Forms

- [wagtailpolls](https://github.com/takeflight/wagtailpolls) - A plugin for adding polling capabilities to the Wagtail CMS.
- [Wagtailsurveys](https://github.com/torchbox/wagtailsurveys) - A module for Wagtail which provides the ability to build polls and surveys.
- [Wagtail ReCaptcha](https://github.com/springload/wagtail-django-recaptcha) - wagtail-django-captcha provides an easy way to integrate the [django-recaptcha](https://github.com/praekelt/django-recaptcha) field when using the Wagtail formbuilder.

### Misc

- [wagtail-linkchecker](https://github.com/takeflight/wagtail-linkchecker) - A tool to assist with finding broken links on your Wagtail site.
- [Wagtail Plus](https://github.com/rfosterslo/wagtailplus) - Modular add-ons for Wagtail CMS.
- [wagtailmenus](https://github.com/rkhleics/wagtailmenus) - An extension for Torchbox's Wagtail CMS to help you manage and render multi-level navigation and simple flat menus in a consistent, flexible way.
- [Wagtail Error Pages](https://github.com/alexgleason/wagtailerrorpages) - Pretty, smart, customizable error pages for Wagtail.
- [wagtail-metadata](https://github.com/takeflight/wagtail-metadata) - A tool to assist with metadata for social media and search engines.
- [Wagtail Analytics](https://github.com/tomdyson/wagalytics) - A Google Analytics dashboard in your Wagtail admin.
- [Django Wagtail Feeds](https://github.com/chrisdev/django-wagtail-feeds) - Add support for RSS Feeds, Facebook Instant Articles and Apple News Publisher to your Wagtail CMS Projects.

## Tools

- [Wagtail Cookiecutter Foundation](https://github.com/chrisdev/wagtail-cookiecutter-foundation) - A Cookiecutter template for Wagtail CMS using Zurb Foundation 6.

## Resources

### Getting started

- [Introducing Wagtail
](https://www.springload.co.nz/blog/introducing-wagtail/) - During the last few months we have spent a good amount of time working with Wagtail, a really cool CMS built on top of the well-known Django framework.
- [Getting started in Wagtail, a newcomer's perspective
](https://wagtail.io/blog/getting-started-wagtail-newcomers-perspective/) - Having used Drupal almost exclusively as my main tool of choice for a while now, I was asked to put together a build using Wagtail. By [@kiwimind](https://twitter.com/kiwimind)
- [Présentation de Wagtail, le dernier CMS Django
](http://makina-corpus.com/blog/metier/2016/presentation-de-wagtail-le-dernier-cms-django) - Wagtail est un CMS relativement récent dans l’écosystème Django. Pour autant, son jeune âge ne l’empêche pas de posséder de nombreuses fonctionnalités que nous découvrirons dans cet article.

### Articles

- [Interactive 360 degree product views as a Wagtail streamfield block](http://www.djangopaths.com/interactive-360-degree-product-views-wagtail-streamfield-block/)

### Recipes

- [Oscar Wagtail demo project](https://github.com/LUKKIEN/oscar-wagtail-demo) - A Django recipe for integrating Oscar E-commerce into a Wagtail CMS application.

### Presentations

- [An Introduction to Wagtail](https://www.youtube.com/watch?v=glIIF-kBXf0) by Eloise "Ducky" Macdonald-Meyer - This talk is an introduction to Wagtail, a content management system built on the Python web framework, Django.
- [DjangoCon US 2015 - Wagtail - Yet Another Django CMS](https://www.youtube.com/watch?v=6j0NVq6g4FE) by Tom Dyson - Tom will explain why his agency decided to build a new CMS, share some lessons learned in running a growing open source project, and outline Wagtail's roadmap to version 2 and beyond. [Slide deck](https://speakerdeck.com/tomdyson/wagtail-yet-another-cms-djangocon-us-2015)
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

### Meetups

- [Bristol Wagtail Users and Developers](https://www.meetup.com/Bristol-Wagtail-Users-and-Developers/) - The South West group (nest?) of people who work with Wagtail CMS.
- [Dutch Wagtail Meetup](http://www.meetup.com/Dutch-Wagtail-Meetup/) - This is a group for anyone interested in working and developing with Wagtail.
- [Wellington Wagtail CMS Meetup](http://www.meetup.com/Wellington-Wagtail-CMS-Meetup/) - The first Wagtail CMS meetup in New Zealand!

## Contribute

Contributions are always welcome!
Please read the [contribution guidelines](CONTRIBUTING.md) first.

## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Springload](https://www.springload.co.nz/) has waived all copyright and related or neighboring rights to this work.
