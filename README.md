# interview_assistant
Repository attempting to aid interviewers in making good interviews

*Basic Idea*

Interviews are generally haphazard, with many different people asking many different questions and generally just making them up. People bring all their biases. 
People don't ask orthogonal questions, that gain lot's of different bits of info but go too deep, or oppositely, they ask many shallow questions, but test nothing
deeply.

*Solution*
A curated wiki list of interview questions. Anyone can add to. Questions are rated on effectiveness, time taken, and a vector of typeness of question, what is it testing.
Users who provide questions with high ratings get some reward. 
Users who rate things etc get some badges or something.
(^^above is just game mechanics design to incentivise useful behaviour.)

UX is: 
1. Open the page, choice of questions, like:
	How long are you interviewing for
	Name of Job you are hiring for.
	Salary band you are hiring to.
	Your experience as an interviewer.
	What topics/ themes you want to ask about/ job requirements.
	As you answer questions:....
		_Cool to be able to just feed in job requirements spec and let it auto read_
2. A live feed of suggested questions/topic areas - maybe top 3 topic areas with top 3 qs from each, and a button to pick all 3, or just some of them.

The live feed will update off the answers to the questions. Can use RNNs for this according to Monzo article on RNNs. I.e use user choices to predict what they will want to see. 

3. As you pick questions a little bar on the side will fill up showing if you have enough or too many. When you get to enough you stop!
	There are also some other meta metrics like:
		How diverse are questions.
		Challenge rank of interview, vs role as described. 
		

4. Review and output, provides a printable PDF of your interview plan, a timing guide, scoring mechanism and so on. 

There is also an 'other' category so that you can capture the ways that you went off track and how the candidate did in this section. 

5. Capture output back into system. Initially manual, later do with QR code and visual interpretation by computer - use google machine vision.

6. Provide comparison graphs on all the candidates, how did they performn on each category, ranks on different strengths with certainties based on #qs asked and degree of deviation from the norm. 
  
7. Suggest topics and areas to ask about on second interview. 


*Later Features*
When you start having organisations, you can say things like, this question, or topic is generally important in this company. This skill or area is what we 
seem to be hiring for. 