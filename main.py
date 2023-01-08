from flask import Flask, render_template
import utils


app = Flask(__name__, template_folder='templates')

@app.route('/')
def page_list():
    candidates = utils.load_candidates_from_json()
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int:pk>')
def page_candidate(pk):
    candidate = utils.get_candidate(pk)
    return render_template('candidate.html', candidate = candidate)


@app.route('/search/<candidate_name>/')
def page_search(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    number_of_candidates = len(candidates)
    return render_template('search.html',
                            candidates=candidates,
                            number_of_candidates=number_of_candidates
                            )

@app.route('/skill/<skill_name>/')
def page_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    number_of_candidates = len(candidates)
    return render_template('skill.html',
                            candidates=candidates,
                            skill_name=skill_name,
                            number_of_candidates=number_of_candidates
                           )


app.run(host='127.0.0.1', port=800, debug=True)