from flask import Flask, request, jsonify
from models import db, SeoResult
from scraper import scrape_seo_data
import os

app = Flask(__name__)

# --- Database Configuration ---
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

# --- API Routes ---

@app.route('/scrape', methods=['POST'])
def scrape_and_save():
    """
    Receives a URL, scrapes SEO data, saves it to the DB, and returns the result.
    """
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({"error": "URL not provided"}), 400

    url = data['url']
    seo_data = scrape_seo_data(url)

    if not seo_data:
        return jsonify({"error": "Failed to scrape the website"}), 500

    # Save the result to the database
    new_result = SeoResult(
        url=seo_data['url'],
        title=seo_data['title'],
        meta_description=seo_data['meta_description'],
        h1_header=seo_data['h1_header'],
        h2_headers=seo_data['h2_headers'],
        word_count=seo_data['word_count']
    )
    db.session.add(new_result)
    db.session.commit()

    return jsonify(new_result.to_dict()), 201

@app.route('/results', methods=['GET'])
def get_all_results():
    """
    Returns all the saved SEO analysis results.
    """
    results = SeoResult.query.all()
    return jsonify([result.to_dict() for result in results])

if __name__ == '__main__':
    app.run(debug=True)
