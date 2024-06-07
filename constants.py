PROMPT_TEXT = """
Generate prefill data for the organization '{{org_name}}' in a valid YAML format that can be converted to a json dictionary. Include these fields and keep the field names as they are, don't change them to lower case with underscore:
- Organization Name
- About the Organization
- Year Founded
- Head Office Location
- Country
- Geographic Reach
- Organization Size - Number of members / employees
- Organization Size - Country Chapters
- Area of Expertise
- Area of Expertise Theme
- Issue Focus Areas
- IPCC Theme / Topic Context
- Partner Organizations
- Total Funding
- Funding Sources
- Government Funding
- Private Funding
- Founder
- Board Members
- Connection to First-response Organizations / Climate Emergency Relief Support
- Academic Institute Collaborations
- Current AI Related Project
- Potential for AI research integration
- Campaigns
- Conferences and Event Participation
- Papers and books published
- Link to the Website
- Data Sources
"""