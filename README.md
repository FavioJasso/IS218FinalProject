# Health & Fitness Supplements — IS218 Group 3 Final Project
Author of Read Me : Favio Jasso 

A Django web application that showcases health and fitness supplements (vitamins,
protein powders, pre-workouts) and lets users rate and review them. Administrators
can manage the catalog and view an aggregated feedback report.

> **For the grader:** jump to [Grader walkthrough](#grader-walkthrough) for a
> step-by-step demo path, then [Specification compliance](#specification-compliance)
> for a checklist mapping each requirement to where it lives in the code.

---

## Team

| Role | Member |
|---|---|
| Project Manager | Lucia Lacourtna |
| Systems Analyst | Favio Jasso |
| Developer | Gabrielle Madric |
| Developer | Jeff Janvier |
| Developer | Lewis Macasaet |

---

## Quick start

### Prerequisites

- Python 3.10 or newer (3.12 recommended; tested on 3.12.12)
- `pip` and `venv` (ship with Python)
- Git

### macOS / Linux

```bash
# 1. Clone and enter the repo
git clone https://github.com/FavioJasso/IS218FinalProject.git
cd IS218FinalProject

# 2. Create + activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. Create the project's demo admin account (idempotent — safe to re-run)
python manage.py ensure_admin
#   This creates user "IS218" with password "ProjectIS218" — see "Admin
#   credentials" below. To use your own credentials instead, run
#   `python manage.py createsuperuser`.

# 6. Start the development server
python manage.py runserver
```

### Windows (Command Prompt)

```bat
git clone https://github.com/FavioJasso/IS218FinalProject.git
cd IS218FinalProject

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py ensure_admin
python manage.py runserver
```

### Admin credentials

After running `python manage.py ensure_admin` you can sign in to
<http://127.0.0.1:8000/admin/> with:

| Field | Value |
|---|---|
| Username | `IS218` |
| Password | `ProjectIS218` |

The `ensure_admin` management command lives in
`backend/accounts/management/commands/ensure_admin.py`. It is idempotent —
running it again resets the password and the staff/superuser flags, so the
above credentials always work even if the account was edited or the database
was rebuilt. To use a different username or password (for example in CI or
when deploying), pass flags or set environment variables:

```bash
python manage.py ensure_admin --username myadmin --password 'mypassword'
# or
DJANGO_ADMIN_USERNAME=myadmin DJANGO_ADMIN_PASSWORD='mypassword' python manage.py ensure_admin
```

> **Security note:** these are demo credentials for a class project running on
> a local development server. Do **not** reuse this password anywhere real and
> do **not** deploy this project to the public internet without changing it
> (along with `SECRET_KEY` and `DEBUG` in `site_configurations/settings.py`).

The site will be available at **http://127.0.0.1:8000/**. Stop the server with
`Ctrl+C`.

---

## Grader walkthrough

A complete demo of the four required features takes about 5 minutes.

### 1. Browse products (Product display)

1. Open <http://127.0.0.1:8000/>.
   - You should see the homepage hero and feature cards.
2. Click **Catalog** in the navbar (or the "Browse the catalog" button).
   - URL: `/catalog/`.
   - You should see a responsive grid of **8 supplements** with images, names,
     and prices.
3. Click **See details** on any product (for example, *Vitamin C*).
   - URL: `/catalog/item/1/`.
   - The product detail page shows: name, image, synthesized description,
     price, manufacturer, expiration date, in-stock count, and product ID.

### 2. Leave user feedback (rating + comment)

1. Still on a product detail page, scroll down to **Leave a review**.
2. Fill in:
   - *Display name* (optional — leave blank to post as "Anonymous")
   - *Rating* — pick a number of stars from the dropdown
   - *Your review* — write a comment
3. Click **Submit review**.
   - You'll be redirected to the same product page.
   - Your review now appears under **User feedback** with star rating, comment,
     date, and a recomputed average.
4. Click **Feedback** in the navbar.
   - URL: `/feedback/`.
   - This public hub shows total review count, overall average, top-rated
     products, and the 20 most recent reviews across the whole catalog.

> **No login is required** to leave a review (matching the spec's "comment box"
> language). If you *are* logged in as a staff member, your name is captured
> automatically.

### 3. Admin functionality (Add / edit / delete products, view feedback)

1. Open <http://127.0.0.1:8000/admin/> and sign in with the demo credentials
   created by `python manage.py ensure_admin`:
   - **Username:** `IS218`
   - **Password:** `ProjectIS218`
2. After signing in, the navbar will show two new links: **Report** and **Admin**.
3. From the admin index, you can manage:
   - **Accounts → Products** — add, edit, or delete catalog products.
     (`/admin/accounts/product/`)
   - **Accounts → Inventories** — manage stock counts.
   - **Accounts → Log comments** — moderate the legacy comment system.
   - **Pages → Product reviews** — view, edit, or delete any user rating + comment.
     (`/admin/pages/productreview/`)
   - **Pages → Vitamin reviews** — standalone vitamin reviews not tied to a product.
   - **Pages → Admin feedback** — internal admin-to-admin feedback (separate from
     user feedback).
4. Try the full CRUD cycle on a product:
   - Click **Add product +**, fill in the fields, save.
   - The new product immediately appears at `/catalog/`.
   - Edit it from the admin and refresh the catalog.
   - Delete it from the admin and refresh the catalog.

### 4. Admin-only feedback report

1. While signed in as a staff user, click **Report** in the navbar (or visit
   <http://127.0.0.1:8000/admin-report/feedback/>).
2. The report shows:
   - Top-of-page **stat tiles**: total product reviews, total legacy comments,
     standalone vitamin reviews, and the overall average rating.
   - A **per-product section** grouping every rating, comment, and review under
     each catalog product, with that product's average rating and review count.
   - A trailing section listing standalone vitamin reviews not tied to a product.
3. Sign out and try the same URL anonymously — you should be redirected to the
   admin login page (`@staff_member_required`).

---

## Specification compliance

Every line of the specification mapped to where it is implemented.

### Working application

| Requirement | Where to find it |
|---|---|
| Working application | The whole repo — runs end-to-end via `python manage.py runserver`. |

### Product display

| Requirement | Where to find it |
|---|---|
| Minimum of 8 products | Seeded in `db.sqlite3` (`accounts.Product` table). Verify on `/catalog/`. |
| Product list page | `/catalog/` → view: `backend.accounts.views.catalog`; template: `frontend/templates/pages/catalog/catalog.html`. |
| Product detail (name) | Rendered in `pages/catalog/item_info.html`. |
| Product detail (description) | Synthesized from `product_type` + `dosage_amount` + `formula_type` + `manufacturer` in `_build_product_description()` in `backend/accounts/views.py`. |
| Product detail (image) | Dynamic lookup against `frontend/static/images/media/supplement_images/` via `_image_url_for_product()` in `backend/accounts/views.py`. |
| Product detail (price) | `product.price` rendered in `pages/catalog/item_info.html`. |

### User feedback

| Requirement | Where to find it |
|---|---|
| Rating system (stars or numeric) | `pages.ProductReview.rating` (`IntegerField` 1–5 with star choices). Stars rendered via the `ProductReview.stars` property. |
| Comment box | `pages.ProductReview.comment` + `ProductReviewForm` in `backend/pages/forms.py`. |
| Display feedback (blog-style under each product) | "User feedback" section of `pages/catalog/item_info.html` — review cards with author, star rating, comment, and date. |

### Admin functionality

| Requirement | Where to find it |
|---|---|
| Admin login | Standard Django admin at `/admin/`. |
| Add, edit, delete products | `Product` registered with `ProductAdmin` in `backend/accounts/admin.py`. URL: `/admin/accounts/product/`. |
| View user feedback | `ProductReview` registered with `ProductReviewAdmin` in `backend/pages/admin.py`. URL: `/admin/pages/productreview/`. Legacy `LogComment` and standalone `VitaminReview` are also registered. |

### Feedback report (admin-only)

| Requirement | Where to find it |
|---|---|
| Admin-only page showing all feedback comments | View: `feedback_report` in `backend/pages/views.py` (decorated with `@staff_member_required`). Template: `frontend/templates/pages/feedback_report.html`. URL: `/admin-report/feedback/`. |
| Admin-only page showing all ratings | Same page — every product is listed with its review count, average rating, individual ratings, and comments. |

### Technical requirements — Models

| Requirement | Where to find it |
|---|---|
| Product model (name, description, price, image) | `backend/accounts/models.py` — `Product` (`product_name`, `price`, etc.). The `Product` table is `managed = False` (lives in `db.sqlite3` as a pre-existing schema), so `description` is synthesized at the view layer and `image` is matched by filename to `frontend/static/images/media/supplement_images/`. |
| Feedback model (product FK, rating, comment) | `backend/pages/models.py` — `ProductReview` (`product_id`, `user`, `display_name`, `rating`, `comment`, `created_at`). `product_id` is an `IntegerField` (not a `ForeignKey`) because `Product` is `managed = False` with a non-default primary-key column; lookups use `Product.objects.get(pk=...)`. Migration: `backend/pages/migrations/0003_productreview.py`. |

### Technical requirements — Views

| Requirement | Where to find it |
|---|---|
| Product list view | `backend.accounts.views.catalog`. |
| Product detail view | `backend.accounts.views.item_info`. |
| Feedback submission view | `backend.pages.views.submit_product_review` at `/catalog/item/<pk>/review/` (also rendered inline at the bottom of every product detail page). |
| Admin-only feedback report view | `backend.pages.views.feedback_report` at `/admin-report/feedback/`. |

### Technical requirements — Templates

| Requirement | Where to find it |
|---|---|
| Base layout | `frontend/templates/layout.html` (sticky header, main content slot, footer). |
| Product list | `frontend/templates/pages/catalog/catalog.html`. |
| Product detail | `frontend/templates/pages/catalog/item_info.html`. |
| Feedback report | `frontend/templates/pages/feedback_report.html`. |

### Technical requirements — Forms

| Requirement | Where to find it |
|---|---|
| Feedback submission form | `ProductReviewForm` in `backend/pages/forms.py`. |

### Technical requirements — Admin Panel

| Requirement | Where to find it |
|---|---|
| Register Product model | `ProductAdmin` in `backend/accounts/admin.py`. |
| Register Feedback model | `ProductReviewAdmin` in `backend/pages/admin.py`. |

---

## Architecture overview

```
IS218FinalProject/
├── manage.py                     # Django entry point
├── requirements.txt              # Python dependencies (Django 5.2)
├── db.sqlite3                    # SQLite database (8 seeded products)
├── site_configurations/          # Django project (settings, root urls)
│   ├── settings.py
│   └── urls.py
├── backend/
│   ├── accounts/                 # Catalog + product detail + log comments
│   │   ├── models.py             # Product, Inventory, LogComment, AuthUser, ...
│   │   ├── views.py              # catalog, item_info, feedback hub, log_comment
│   │   ├── urls.py
│   │   └── admin.py              # Product/Inventory/LogComment admin registration
│   └── pages/                    # Reviews + admin feedback report
│       ├── models.py             # ProductReview, VitaminReview, AdminFeedback
│       ├── forms.py              # ProductReviewForm, VitaminReviewForm, ...
│       ├── views.py              # submit_product_review, feedback_report, ...
│       ├── urls.py
│       ├── admin.py              # ProductReview/VitaminReview/AdminFeedback admin
│       └── migrations/
│           ├── 0001_initial.py             # VitaminReview
│           ├── 0002_adminfeedback.py       # AdminFeedback
│           └── 0003_productreview.py       # ProductReview (the spec model)
├── frontend/
│   ├── static/
│   │   ├── css/                  # main.css + navbar.css design system
│   │   └── images/media/supplement_images/   # product images
│   └── templates/
│       ├── layout.html           # base template
│       ├── accounts/             # login, register, ratings, ...
│       └── pages/
│           ├── index.html        # home
│           ├── about.html
│           ├── feedback.html              # public feedback hub
│           ├── feedback_report.html       # admin-only report
│           ├── submit_product_review.html # standalone submit form
│           └── catalog/
│               ├── catalog.html
│               └── item_info.html         # product detail + reviews
└── README.md                     # this file
```

### URL map (most important routes)

| URL | What it is | Access |
|---|---|---|
| `/` | Homepage hero + feature cards | Public |
| `/catalog/` | Product grid | Public |
| `/catalog/item/<pk>/` | Product detail + review form | Public |
| `/catalog/item/<pk>/review/` | Standalone review submission | Public |
| `/feedback/` (and `/accounts/feedback/`) | Public feedback hub (recent reviews, top rated) | Public |
| `/reviews/` | Standalone vitamin reviews list | Public |
| `/submit-rating/` | Standalone vitamin review form | Public |
| `/admin/` | Django admin (catalog CRUD + moderation) | Staff only |
| `/admin-report/feedback/` | Aggregated user-feedback report | Staff only |

---

## Tech stack

- **Python** 3.12 (3.10+ supported)
- **Django** 5.2 (`requirements.txt`)
- **SQLite** for the database (file: `db.sqlite3`)
- **HTML / CSS** — no JavaScript framework. Custom CSS design system in
  `frontend/static/css/main.css` (CSS variables, system font stack, responsive
  grid, sticky header, card components, star-rating widget).

---

## Troubleshooting

**`OperationalError: no such table: pages_productreview`**
You skipped step 4 of the setup. Run:

```bash
python manage.py migrate
```

**The site loads but has no styling**
Force a hard refresh in the browser (`Cmd+Shift+R` on macOS, `Ctrl+F5` on
Windows) to clear cached CSS.

**`python` is not recognized / wrong Python version**
Use `python3` instead of `python` on macOS/Linux. Verify with
`python3 --version` — it must be 3.10 or newer.

**Port 8000 is already in use**
Run on a different port: `python manage.py runserver 8001`.

**No images appear on product pages**
Make sure the directory `frontend/static/images/media/supplement_images/` exists
and contains image files. The view matches product names to filenames in that
folder.

---

## Project documents (in this repo)

- `PROJECT_REQUIREMENTS.md` — copy of the assignment specification.
- `README.md` — this file (run instructions + grader walkthrough).
