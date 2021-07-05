# The Weeknd's lyrics analysis
hey 👋🏽

P.S. I'm actually writing an article on medium about this project, but I'm updating the README here while I procrastinate the article.

### 🚨 there ARE photos below in case you don't want to read this gigantic essay 🚨

In this project I leveraged various data science and web development technologies making it almost "end to end", rendering it one of my personal favourite projects I've made. 

To start off, The Weeknd is one of my favourite performing artists (hopefully one day I get to go to a concert 😞) and one thing I always get into debates with my other Weeknd fanboy friends is how his music has changed from his earlier recordings to his more modern releases. So I decided it would be a perfect opportunity to try out some data science technologies and investigate that shift, and then deploy some of my findings for more people to play around with. 

I have the major components of the project flow seperated into their different folders as you can see from `data_collection`, etc., but to walk through the main parts, I started with collecting essentially ALL of The Weeknd's lyrics that I could find on Genius using it's API (even unreleased songs). After some preliminary filtering and cleaning, we're ready to properly process it to conduct some experimentation. There is a Jupyter Notebook in the `data_science` folder, but I usually come back often and run some extra "mini-tests" whenever I'm bored and curious, in case you want to see the completely 'live' version, you can access it [here](https://colab.research.google.com/drive/1QSMTCNu69TH1PJ-Ktc1m5JTYz_bzvDRF?usp=sharing). In advance, it's a very messy notebook so my best wishes in case you actually try to go through it. In there, I run some more processing like lemmatization, stop word removal, ..., so we can get the data in the right format to run some analysis on. You'll see a lot of colourful graphs and charts going through it that display key and essential features such as frequencies of various subjects and sentiment analysis. The most special one being the topic modelling, which is a NLP method that tries to determine different topics in the documents depending on distribution of various words and grouping them together. In case you want to learn more, I found [this article](https://monkeylearn.com/blog/introduction-to-topic-modeling/) to be fantastic. Thereafter, I basically squeezed all the data into an LSTM based deep learning model that could generate The Weeknd's lyrics based off the initial seed and temperature you give it. The most interesting part being the ability to filter between text generation from the "old" Weeknd and the "new" Weeknd.

Then to actually push this to the world, I saved this model and deployed it via AWS Elastic Beanstalk through a Flask based REST API, and a React frontend. I had it up for approximately 2-3 days but I ended up taking it down because I was running out of my student AWS credits a bit too quickly 😞. Here's some pictures of what it looked like though in case you were curious.

![](/img/img1.png)
![](/img/img2.png)
![](/img/img3.png)
![](/img/img4.png)
![](/img/img5.png)

In retrospect, I feel like there's still a lot of additions that I keep wanting to make to the project, e.g. it would be extremely interesting to make a "personal board" kind of app where you can pin your favourite seed and generated lyrics.

In case anyone reading this has any questions about literally anything, please feel free to reach out dhyeylalseta@outlook.com or message me on Linkedin, I'd be more than happy to speak out more about this project. Thank you for the time!