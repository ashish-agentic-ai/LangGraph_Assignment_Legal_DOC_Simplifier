# LangGraph Parallel-Workflow Assignment

## Overview

You have been given a working LangGraph project - **Mental Wellness Practice
Suggester** - as your reference implementation. Your task is to build your own
unique use case using the same framework and graph pattern.

Study `mental_wellness_graph.py` carefully. Your graph must follow a similar
structure:

```text
[User Input] -> [Understand / Classify Input]
                     |
                     +-> [Specialist Node 1] --+
                     +-> [Specialist Node 2] --+-> [Decision Node] -> [Conditional Final Output]
                     +-> [Specialist Node 3] --+
```

---

## What You Must Build

Using the same LangGraph patterns from the reference code:

- `StateGraph` - to create the graph
- A Pydantic state model - to define data fields
- Node functions - each node must do one clear job
- At least 3 parallel specialist nodes
- One decision node that reads all specialist outputs
- One conditional routing function
- At least 2 possible final output nodes
- `ChatOpenAI` - for LLM-based reasoning
- A `run_<your_project>()` function - as the main entry point

Your graph should not copy the mental wellness use case. Use the same pattern,
but build your assigned project.

---

## Submission Steps

1. Fork or clone this repo to your local machine.
2. Create your own Python file, for example `resume_review_graph.py`.
3. Do not modify `mental_wellness_graph.py`.
4. Build your assigned use case using the same LangGraph structure.
5. Test it end-to-end with your OpenAI key.
6. Push your code to a new public GitHub repository under your own account.
7. Share the GitHub link in the Excel sheet shared on WhatsApp.

Your repo must contain:

- Your LangGraph `.py` file
- A `requirements.txt`
- A `.env.example` file
- A `.gitignore`
- A `README.md` explaining what your graph does and how to run it

Never commit your real `.env` file or API key.

---

## Individual Assignments

---

### 1. Chan Wei Khjan - Resume Reviewer Graph

**Use Case:** A user pastes resume text and a job description. The graph reviews
the resume and recommends improvements.

**Specialist Node 1 - `check_skills_match`**
- Identify matching and missing skills.

**Specialist Node 2 - `check_experience_alignment`**
- Compare work experience with job requirements.

**Specialist Node 3 - `check_resume_keywords`**
- Suggest important keywords missing from the resume.

**Decision Node:** Decide whether the resume needs minor edits or major rewrite.

**Final Nodes:** `minor_resume_edits` and `major_resume_rewrite_plan`.

---

### 2. Gurleen Kaur - Recipe Planner Graph

**Use Case:** A user provides ingredients available at home. The graph suggests
what to cook.

**Specialist Node 1 - `suggest_main_dish`**
- Suggest a dish using the available ingredients.

**Specialist Node 2 - `suggest_side_or_drink`**
- Suggest a simple side dish or drink.

**Specialist Node 3 - `check_missing_staples`**
- Identify 1-2 common pantry items that may be needed.

**Decision Node:** Decide whether the recipe is quick or detailed.

**Final Nodes:** `quick_recipe_card` and `detailed_cooking_plan`.

---

### 3. Komal Patil - Code Explainer Graph

**Use Case:** A user pastes code. The graph explains, reviews, and comments it.

**Specialist Node 1 - `explain_code_plain_english`**
- Explain what the code does.

**Specialist Node 2 - `identify_code_risks`**
- Identify bugs, edge cases, or unclear parts.

**Specialist Node 3 - `add_code_comments`**
- Return the code with helpful inline comments.

**Decision Node:** Decide whether the code needs simple explanation or deeper review.

**Final Nodes:** `simple_code_explanation` and `deep_code_review`.

---

### 4. Anived Mishra - Story Writer Graph

**Use Case:** A user provides a story idea. The graph develops it into a story.

**Specialist Node 1 - `create_characters`**
- Create main characters.

**Specialist Node 2 - `create_plot_outline`**
- Create beginning, middle, and ending.

**Specialist Node 3 - `create_setting_and_tone`**
- Define setting, mood, and genre.

**Decision Node:** Decide whether to write a short story or expanded story.

**Final Nodes:** `write_short_story` and `write_expanded_story`.

---

### 5. Lalit Jain - SQL Helper Graph

**Use Case:** A user describes the data they need. The graph generates SQL and
explains it.

**Specialist Node 1 - `identify_tables`**
- Infer likely tables and fields.

**Specialist Node 2 - `generate_sql_query`**
- Write a clean SQL query.

**Specialist Node 3 - `check_sql_risks`**
- Check for missing filters, joins, or assumptions.

**Decision Node:** Decide whether the query is simple or advanced.

**Final Nodes:** `simple_sql_response` and `advanced_sql_response`.

---

### 6. Gurkamal Singh - Product Copywriter Graph

**Use Case:** A user gives a product name and features. The graph creates
product copy.

**Specialist Node 1 - `write_feature_summary`**
- Summarize product features.

**Specialist Node 2 - `write_benefit_summary`**
- Convert features into customer benefits.

**Specialist Node 3 - `identify_target_customer`**
- Identify the likely buyer persona.

**Decision Node:** Decide whether the output should be formal or marketing-heavy.

**Final Nodes:** `formal_product_description` and `marketing_product_copy`.

---

### 7. Joseph - Meeting Notes Graph

**Use Case:** A user pastes messy meeting notes. The graph organizes them.

**Specialist Node 1 - `extract_discussion_points`**
- Extract important discussion topics.

**Specialist Node 2 - `extract_decisions`**
- Extract decisions made.

**Specialist Node 3 - `extract_action_items`**
- Extract owners, tasks, and deadlines.

**Decision Node:** Decide whether notes are complete or missing key details.

**Final Nodes:** `complete_meeting_summary` and `meeting_summary_with_gaps`.

---

### 8. Siddhesh Sawant - Travel Planner Graph

**Use Case:** A user provides a destination and trip length. The graph creates a
travel plan.

**Specialist Node 1 - `suggest_sightseeing`**
- Suggest attractions.

**Specialist Node 2 - `suggest_food_experiences`**
- Suggest food and restaurant experiences.

**Specialist Node 3 - `suggest_culture_or_adventure`**
- Suggest cultural or adventure activities.

**Decision Node:** Decide whether the trip style is relaxed or packed.

**Final Nodes:** `relaxed_itinerary` and `packed_itinerary`.

---

### 9. Karthik Balaje R - Interview Coach Graph

**Use Case:** A user provides a job role. The graph prepares interview practice.

**Specialist Node 1 - `generate_technical_questions`**
- Generate technical questions.

**Specialist Node 2 - `generate_behavioral_questions`**
- Generate behavioral questions.

**Specialist Node 3 - `generate_role_specific_questions`**
- Generate questions specific to the role.

**Decision Node:** Decide whether the candidate needs beginner or advanced prep.

**Final Nodes:** `beginner_interview_pack` and `advanced_interview_pack`.

---

### 10. Sai Sankar - Social Media Post Graph

**Use Case:** A user provides an announcement. The graph converts it into social
content.

**Specialist Node 1 - `write_formal_announcement`**
- Write a professional announcement.

**Specialist Node 2 - `create_social_hook`**
- Write hook options.

**Specialist Node 3 - `suggest_hashtags`**
- Suggest relevant hashtags.

**Decision Node:** Decide whether the tone should be professional or playful.

**Final Nodes:** `linkedin_style_post` and `instagram_style_post`.

---

### 11. Bala Krishna Yenumula - Bug Report Analyzer Graph

**Use Case:** A user pastes a bug report or error message. The graph analyzes
the issue.

**Specialist Node 1 - `identify_possible_causes`**
- List likely causes.

**Specialist Node 2 - `suggest_logs_to_check`**
- Suggest logs, files, or commands to inspect.

**Specialist Node 3 - `estimate_severity`**
- Classify severity and user impact.

**Decision Node:** Decide whether the issue is low priority or urgent.

**Final Nodes:** `standard_debug_plan` and `urgent_debug_plan`.

---

### 12. Beadon Roy - Study Notes Graph

**Use Case:** A user provides a study topic. The graph creates learning
material.

**Specialist Node 1 - `explain_core_concepts`**
- Explain key concepts.

**Specialist Node 2 - `generate_examples`**
- Provide examples or analogies.

**Specialist Node 3 - `create_quiz_questions`**
- Create practice questions.

**Decision Node:** Decide whether the learner needs beginner or advanced notes.

**Final Nodes:** `beginner_study_pack` and `advanced_study_pack`.

---

### 13. Sagar Sable - Job Description Writer Graph

**Use Case:** A user provides a job title and requirements. The graph writes a
job description.

**Specialist Node 1 - `write_role_overview`**
- Draft the role overview.

**Specialist Node 2 - `write_responsibilities`**
- Draft responsibilities.

**Specialist Node 3 - `write_requirements`**
- Draft requirements and qualifications.

**Decision Node:** Decide whether the JD should be formal or candidate-friendly.

**Final Nodes:** `formal_job_description` and `engaging_job_post`.

---

### 14. Ankith Dasu - Customer Complaint Graph

**Use Case:** A user pastes a customer complaint. The graph classifies and
responds to it.

**Specialist Node 1 - `classify_complaint_category`**
- Classify the complaint type.

**Specialist Node 2 - `classify_complaint_severity`**
- Determine severity.

**Specialist Node 3 - `suggest_resolution_path`**
- Suggest next steps.

**Decision Node:** Decide whether normal support or escalation is needed.

**Final Nodes:** `standard_customer_response` and `escalation_response`.

---

### 15. Tilottama Pawar - Personal Finance Graph

**Use Case:** A user provides income, expenses, and a financial goal. The graph
creates a finance plan.

**Specialist Node 1 - `analyze_income_expenses`**
- Summarize monthly money flow.

**Specialist Node 2 - `identify_savings_opportunities`**
- Find places to reduce spending.

**Specialist Node 3 - `plan_goal_timeline`**
- Estimate a realistic timeline.

**Decision Node:** Decide whether the goal is easy or challenging.

**Final Nodes:** `simple_savings_plan` and `strict_savings_plan`.

---

### 16. Mini Yadav - Fitness Plan Graph

**Use Case:** A user provides a fitness goal and current level. The graph
creates a workout plan.

**Specialist Node 1 - `suggest_cardio_plan`**
- Suggest cardio activities.

**Specialist Node 2 - `suggest_strength_plan`**
- Suggest strength exercises.

**Specialist Node 3 - `suggest_recovery_plan`**
- Suggest rest, mobility, and safety tips.

**Decision Node:** Decide whether the user needs beginner or intermediate plan.

**Final Nodes:** `beginner_fitness_plan` and `intermediate_fitness_plan`.

---

### 17. Purnima Sambasivan - Learning Roadmap Graph

**Use Case:** A user provides a skill they want to learn. The graph creates a
roadmap.

**Specialist Node 1 - `break_down_topics`**
- Break the skill into topics.

**Specialist Node 2 - `suggest_resources`**
- Suggest resource types and practice formats.

**Specialist Node 3 - `create_practice_tasks`**
- Create hands-on practice tasks.

**Decision Node:** Decide whether the roadmap should be beginner or advanced.

**Final Nodes:** `beginner_learning_roadmap` and `advanced_learning_roadmap`.

---

### 18. Jocelyn Jose - Email Composer Graph

**Use Case:** A user provides a recipient, email purpose, and key points. The
graph drafts a professional email ready to send.

**Specialist Node 1 - `analyze_email_intent`**
- Identify the tone, formality level, and goal of the email.

**Specialist Node 2 - `draft_email_body`**
- Write a complete email with subject line, greeting, body, and sign-off.

**Specialist Node 3 - `check_email_completeness`**
- Verify all key points are covered and flag any missing details.

**Decision Node:** Decide whether the email should be concise or a detailed
formal letter based on purpose and recipient.

**Final Nodes:** `concise_email_draft` and `formal_email_draft`.

---

### 19. Kalpesh Gujrati - Blog Outline Graph

**Use Case:** A user provides a blog topic and target audience. The graph builds
a structured blog outline.

**Specialist Node 1 - `suggest_blog_angles`**
- Suggest possible angles or hooks for the topic.

**Specialist Node 2 - `build_section_outline`**
- Draft the main sections and sub-points.

**Specialist Node 3 - `suggest_seo_keywords`**
- Suggest keywords and a working title.

**Decision Node:** Decide whether the blog should be a short post or a long guide.

**Final Nodes:** `short_blog_outline` and `long_form_blog_outline`.

---

### 20. Vishal Ghume - Movie Recommendation Graph

**Use Case:** A user describes their mood and favorite genres. The graph
recommends what to watch.

**Specialist Node 1 - `match_genre_preferences`**
- Match recommendations to preferred genres.

**Specialist Node 2 - `match_mood`**
- Suggest titles that fit the current mood.

**Specialist Node 3 - `check_runtime_and_platform`**
- Consider available time and streaming platforms.

**Decision Node:** Decide whether to suggest a single pick or a watchlist.

**Final Nodes:** `single_movie_pick` and `curated_watchlist`.

---

### 21. Ayush Jain - Presentation Builder Graph

**Use Case:** A user provides a topic and audience. The graph plans a slide deck.

**Specialist Node 1 - `define_key_messages`**
- Identify the core messages to convey.

**Specialist Node 2 - `build_slide_structure`**
- Draft a slide-by-slide structure.

**Specialist Node 3 - `suggest_visuals_and_data`**
- Suggest charts, images, or data per slide.

**Decision Node:** Decide whether the deck should be a quick pitch or a detailed talk.

**Final Nodes:** `quick_pitch_deck` and `detailed_presentation_plan`.

---

### 22. Rahul Bhatia - Startup Idea Validator Graph

**Use Case:** A user describes a startup idea. The graph evaluates and refines it.

**Specialist Node 1 - `analyze_problem_fit`**
- Assess the problem and target customer.

**Specialist Node 2 - `analyze_market_and_competition`**
- Identify market size and competitors.

**Specialist Node 3 - `identify_risks_and_assumptions`**
- List key risks and assumptions to test.

**Decision Node:** Decide whether the idea is promising or needs major rework.

**Final Nodes:** `promising_idea_report` and `idea_rework_plan`.

---

### 23. Swetha KJ - Book Summary Graph

**Use Case:** A user provides a book title or chapter text. The graph creates a
summary.

**Specialist Node 1 - `extract_core_themes`**
- Identify the main themes and ideas.

**Specialist Node 2 - `extract_key_takeaways`**
- Pull out actionable takeaways.

**Specialist Node 3 - `pick_notable_quotes`**
- Highlight memorable quotes or points.

**Decision Node:** Decide whether the reader needs a quick recap or a deep summary.

**Final Nodes:** `quick_book_recap` and `detailed_book_summary`.

---

### 24. Ashish - Legal Document Simplifier Graph

**Use Case:** A user pastes legal or contract text. The graph explains it in
plain language.

**Specialist Node 1 - `explain_clauses_plain_english`**
- Translate clauses into simple language.

**Specialist Node 2 - `identify_obligations`**
- List duties and responsibilities of each party.

**Specialist Node 3 - `flag_risky_terms`**
- Flag risky, unusual, or unclear terms.

**Decision Node:** Decide whether the document is low risk or needs careful review.

**Final Nodes:** `plain_summary_response` and `risk_review_response`.

---

### 25. Gayatri Kumari - Event Planner Graph

**Use Case:** A user provides an event type, budget, and guest count. The graph
plans the event.

**Specialist Node 1 - `plan_venue_and_logistics`**
- Suggest venue, layout, and logistics.

**Specialist Node 2 - `plan_food_and_decor`**
- Suggest catering and decoration ideas.

**Specialist Node 3 - `build_budget_breakdown`**
- Estimate a budget breakdown.

**Decision Node:** Decide whether to plan a simple gathering or a full event.

**Final Nodes:** `simple_event_plan` and `full_event_plan`.

---

### 26. Prajkta Tayade - Outfit Stylist Graph

**Use Case:** A user provides an occasion and wardrobe items. The graph suggests
outfits.

**Specialist Node 1 - `match_outfit_to_occasion`**
- Suggest outfits suited to the occasion.

**Specialist Node 2 - `suggest_color_pairings`**
- Recommend color and pattern combinations.

**Specialist Node 3 - `suggest_accessories`**
- Suggest accessories and footwear.

**Decision Node:** Decide whether the look should be casual or formal.

**Final Nodes:** `casual_outfit_plan` and `formal_outfit_plan`.

---

### 27. Aditya Harvi - Car Buying Advisor Graph

**Use Case:** A user provides their budget, needs, and usage. The graph
recommends a car.

**Specialist Node 1 - `match_cars_to_needs`**
- Shortlist car types that fit the needs.

**Specialist Node 2 - `compare_running_costs`**
- Compare fuel, mileage, and maintenance costs.

**Specialist Node 3 - `check_resale_and_safety`**
- Consider resale value and safety ratings.

**Decision Node:** Decide whether to recommend a budget pick or a premium pick.

**Final Nodes:** `budget_car_recommendation` and `premium_car_recommendation`.

---

### 28. Bharat Chhabriya - Investment Allocation Graph

**Use Case:** A user provides a goal, time horizon, and risk appetite. The graph
suggests an allocation.

**Specialist Node 1 - `assess_risk_profile`**
- Determine the user's risk tolerance.

**Specialist Node 2 - `suggest_asset_mix`**
- Suggest a mix across asset classes.

**Specialist Node 3 - `plan_goal_horizon`**
- Align allocation with the time horizon.

**Decision Node:** Decide whether the strategy should be conservative or aggressive.

**Final Nodes:** `conservative_allocation_plan` and `aggressive_allocation_plan`.

---

### 29. Abhishek Singh - Cybersecurity Risk Advisor Graph

**Use Case:** A user describes a system or app setup. The graph reviews security
risks.

**Specialist Node 1 - `identify_vulnerabilities`**
- Identify likely vulnerabilities.

**Specialist Node 2 - `assess_data_exposure`**
- Assess sensitive data exposure.

**Specialist Node 3 - `recommend_safeguards`**
- Recommend safeguards and best practices.

**Decision Node:** Decide whether the setup is reasonably safe or high risk.

**Final Nodes:** `standard_security_report` and `high_risk_security_report`.

---

### 30. Chetan Gujarathi - API Documentation Graph

**Use Case:** A user pastes API endpoint code or a spec. The graph generates
documentation.

**Specialist Node 1 - `describe_endpoints`**
- Describe each endpoint and its purpose.

**Specialist Node 2 - `document_params_and_responses`**
- Document parameters, requests, and responses.

**Specialist Node 3 - `generate_usage_examples`**
- Provide example requests and responses.

**Decision Node:** Decide whether to produce a quick reference or full docs.

**Final Nodes:** `quick_api_reference` and `full_api_documentation`.

---

### 31. Vinay Dhomane - Git Commit Message Graph

**Use Case:** A user pastes a code diff or change summary. The graph writes a
commit message.

**Specialist Node 1 - `summarize_changes`**
- Summarize what changed in the diff.

**Specialist Node 2 - `classify_change_type`**
- Classify the change (feat, fix, refactor, etc.).

**Specialist Node 3 - `draft_commit_body`**
- Draft the commit body with details.

**Decision Node:** Decide whether a short commit or a detailed commit is needed.

**Final Nodes:** `short_commit_message` and `detailed_commit_message`.

---

### 32. Sanket Hulle - Product Review Summarizer Graph

**Use Case:** A user pastes multiple product reviews. The graph summarizes them.

**Specialist Node 1 - `extract_pros`**
- Extract commonly praised points.

**Specialist Node 2 - `extract_cons`**
- Extract commonly reported problems.

**Specialist Node 3 - `gauge_overall_sentiment`**
- Estimate overall sentiment and rating.

**Decision Node:** Decide whether the product is recommended or not recommended.

**Final Nodes:** `recommended_summary` and `not_recommended_summary`.

---

### 33. Dharma Tekipudi - Language Phrase Coach Graph

**Use Case:** A user provides a target language and a real-life scenario. The
graph teaches useful phrases.

**Specialist Node 1 - `generate_key_phrases`**
- Generate phrases for the scenario.

**Specialist Node 2 - `add_pronunciation_guide`**
- Add simple pronunciation hints.

**Specialist Node 3 - `explain_cultural_tips`**
- Share etiquette and cultural tips.

**Decision Node:** Decide whether the learner needs a beginner or traveler pack.

**Final Nodes:** `beginner_phrase_pack` and `traveler_phrase_pack`.

---

### 34. Durgeshkumar Abbad - Home Renovation Planner Graph

**Use Case:** A user provides a space, budget, and goals. The graph plans the
renovation.

**Specialist Node 1 - `plan_layout_changes`**
- Suggest layout and structural ideas.

**Specialist Node 2 - `plan_materials_and_style`**
- Suggest materials, colors, and style.

**Specialist Node 3 - `estimate_budget_and_timeline`**
- Estimate cost and timeline.

**Decision Node:** Decide whether to plan a refresh or a full remodel.

**Final Nodes:** `budget_refresh_plan` and `full_remodel_plan`.

---

### 35. Akshaykumar More - Podcast Script Graph

**Use Case:** A user provides a podcast topic and format. The graph writes a
script.

**Specialist Node 1 - `draft_intro_hook`**
- Write an opening hook and intro.

**Specialist Node 2 - `build_talking_points`**
- Build the main talking points or segments.

**Specialist Node 3 - `write_outro_and_cta`**
- Write the closing and call-to-action.

**Decision Node:** Decide whether the episode is a short solo or a long interview.

**Final Nodes:** `short_solo_script` and `long_interview_script`.

---

### 36. Upasana Nathsharma - Proposal Writer Graph

**Use Case:** A user describes a project and goal. The graph drafts a proposal.

**Specialist Node 1 - `define_objectives_and_scope`**
- Define objectives, scope, and deliverables.

**Specialist Node 2 - `outline_approach_and_timeline`**
- Outline the approach and timeline.

**Specialist Node 3 - `estimate_cost_and_value`**
- Estimate cost and expected value.

**Decision Node:** Decide whether to produce a short pitch or a formal proposal.

**Final Nodes:** `short_proposal_draft` and `formal_proposal_draft`.

---

### 37. Sourabh Salve - Customer Onboarding Graph

**Use Case:** A user provides a product and a new customer profile. The graph
designs an onboarding plan.

**Specialist Node 1 - `map_first_steps`**
- Map the first key steps for the customer.

**Specialist Node 2 - `plan_education_resources`**
- Suggest guides, tutorials, and resources.

**Specialist Node 3 - `define_success_milestones`**
- Define early success milestones.

**Decision Node:** Decide whether onboarding should be self-serve or guided.

**Final Nodes:** `self_serve_onboarding_plan` and `guided_onboarding_plan`.

---

## Evaluation Criteria

| Criteria | Points |
|---|---:|
| Code follows the same LangGraph structure as `mental_wellness_graph.py` | 20 |
| Uses Pydantic state, `StateGraph`, nodes, edges, and conditional routing correctly | 20 |
| Includes at least 3 parallel specialist nodes | 15 |
| Decision node reads all specialist outputs before routing | 15 |
| Graph runs end-to-end without errors | 10 |
| `README.md` clearly explains the use case and how to run it | 10 |
| GitHub repo is public, clean, and has `.env.example` with no real API key | 10 |
| **Total** | **100** |

---

## Tips

- Run `mental_wellness_graph.py` first before building your own graph.
- Keep every node focused on one responsibility.
- Add one state field for each important output.
- Use `messages: Annotated[list, operator.add]` if you want to track node logs.
- Make your decision node return structured JSON when possible.
- Test simple inputs before testing complex examples.
- Do not push `.env`, `venv`, or `__pycache__` to GitHub.

---

*Deadline and submission link: shared on WhatsApp. Post your GitHub URL in the Excel sheet.*
