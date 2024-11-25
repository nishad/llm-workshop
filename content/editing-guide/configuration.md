---
title: Configuration
weight: 3
---

## Sidebar

### Main Sidebar

For the main sidebar, it is automatically generated from the structure of the content directory.
See the [Organize Files](/editing-guide/organize-files) page for more details.

To exclude a single page from the left sidebar, set the `sidebar.exclude` parameter in the front matter of the page:

```yaml
---
title: Configuration
sidebar:
  exclude: true
---
```

## Right Sidebar

### Table of Contents

Table of contents is automatically generated from the headings in the content file. It can be disabled by setting `toc: false` in the front matter of the page.

```yaml
---
title: Configuration
toc: false
---
```

### Search Index


To exclude a page from the search index, set the `excludeSearch: true` in the front matter of the page:

```yaml
---
title: Configuration
excludeSearch: true
---
```
