# A.S. Computer Education website

Responsive multi-page website for A.S. Computer Education, Jamshedpur. Built with semantic HTML, CSS and vanilla JavaScript; no build step or package install is required.

## Run locally

Run `python3 devserver.py` and open `http://localhost:8000`. The included preview server serves `index.html` for clean page routes so direct links and refreshes work. For deployment, configure equivalent fallback routing on the static host.

## Deploy

Upload this folder to any static host. Configure fallback/rewrite routing so paths such as `/courses` and `/about` serve `index.html`. Set the production canonical domain in `index.html` metadata when domain ownership/configuration is verified. No backend or environment variables are used.

## Enquiry form

The form validates required fields in the browser and prepares a `mailto:` draft for `ascomputer1709@gmail.com`. The visitor must review and send the email. It does not claim successful delivery or store enquiry data. For direct delivery, connect a backend/email provider and implement server-side validation and spam protection before changing the form message.

## Update content

- Course list and descriptions: edit the `courses` array at the top of `app.js`.
- Contact details and course list in rendered pages: update `index.html` and `app.js` consistently.
- Images: replace files in `assets/` while retaining filenames, or update references in `index.html` and `app.js`.
- Header banner: `assets/header-banner.png` is used as the actual image in the header. No additional business-name text is rendered beside it.

Course abbreviations and details remain as supplied; unconfirmed syllabi, duration, fees, eligibility, certifications and outcomes are not asserted.
