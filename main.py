from flask import *
import accounts
import artifacts
import communities

'''
<link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
<script src="{{ url_for('static', filename='script.js') }}" defer></script> <!-- Link to the JavaScript file -->
'''

'''
<h2>Artifacts</h2>
                <ul>
                    {% for artifact in artifactsList %}
                        <li>
                            <h2>Name: {{ artifact.getName() }}</h2>
                            <p>Type: {{ artifact.getType() }}</p>
                            <p>Media:</p><img src="{{ artifact.getMedia() }}" alt="Artifact Media" style="max-width: 300px;">
                            <p>Comments: {{ artifact.getComments() }}</p>
                            <p>Hashtags: {{ artifact.getHashtags() }}</p>
                        </li>
                    {% else %}
                        <p>No artifacts added yet.</p>
                    {% endfor %}

                </ul>
'''

# Create object of Flask
app = Flask(__name__)

account1, account2, account3 = accounts.accounts()
artifactsList = [artifacts.Artifact("Homemade Lamb Biryani", "Food", "https://www.seriouseats.com/thmb/NfZayNEn6JZe9dYH2oBQ7-9UavY=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/lamb-biryani-hero-01-SEA-QIAi-hero-bc09dcc1348f4876bdd2fa1e1a5f918c.JPG", "Made this biryani yesterday. It was so good!", "#biryani #pakistani #food"),
                 artifacts.Artifact("Inspirational Urdu Quote", "Language", "https://media.licdn.com/dms/image/D4D12AQHy0g7DQegQNQ/article-cover_image-shrink_720_1280/0/1708703271331?e=2147483647&v=beta&t=cHoECBqgyBkiJZ4drTvIjmsMVZA8NOsX-yafF4K_V18", "My mom told me this quote means \"the patient fruit is always the sweetest.\" So inspiring!", "#quote #urdu #inspiring")]
foodList, artList, languageList = communities.foodCulture()

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route("/addArtifact.html", methods=['GET', 'POST'])
def addArtifact():

    if request.method == 'POST':

        name = request.form.get('name')
        type = request.form.get('type')
        media = request.form.get('media')
        comments = request.form.get('comments')
        hashtags = request.form.get('hashtags')

        newArtifact = artifacts.Artifact(name, type, media, comments, hashtags)

        artifactsList.append(newArtifact)

        return redirect(url_for('profile'))
    
    return render_template('addArtifact.html')  # Render the HTML form

@app.route("/myProfile.html", methods=['GET', 'POST'])
def profile():

    return render_template('myProfile.html', account1=account1, account2=account2, account3=account3, artifactsList=artifactsList)  # Render the HTML form

@app.route("/home.html")
def home():
    return render_template('home.html')  # Render the HTML form

@app.route("/community.html")
def community():
    return render_template('community.html', foodList=foodList, artList = artList, languageList = languageList)  # Render the HTML form


if __name__ == "__main__":
    app.run(debug=True)
