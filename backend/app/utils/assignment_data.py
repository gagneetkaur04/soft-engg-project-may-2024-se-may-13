from app.models import Assignment, AssignmentQuestion
from app import db

def insert_default_assignments_stats():
    assignment1 = Assignment(
        course_id='MA1002',
        week_number=1
    )
    
    db.session.add(assignment1)
    db.session.commit()

    question1 = AssignmentQuestion(
        assignment_id=assignment1.assignment_id,
        question_text='A quality engineer wants to check the quality of steel rods produced in a steel factory. For this, 40 pieces of steel rods are randomly selected from the steel factory to assess their quality. Based on this, choose the correct option below:',
        option_a=' The population is all steel rods produced in all factories; the sample is the 40 steel rods selected from the given steel factory’s production. ',
        option_b=' The population is all steel rods produced in all factories; the sample is all the steel rods produced in the given steel factory. ',
        option_c=' The population is all steel rods produced in the given steel factory; the sample is the 40 steel rods selected from the given steel factory’s production. ',
        option_d=' All the steel rods in the given steel factory are population; the sample is all steel rods in the given steel factory. ',
        correct_option='c'
    )

    question2 = AssignmentQuestion(
        assignment_id=assignment1.assignment_id,
        question_text='Values of temperature and humidity of a room are measured for 24 hours at a regular time interval of 30 minutes. Based on this, choose the correct option from below:',
        option_a='It is a cross-sectional data',
        option_b='It is a time series data',
        option_c='It is a panel data',
        option_d='It is a longitudinal data',
        correct_option='b'
    )

    question3 = AssignmentQuestion(
        assignment_id=assignment1.assignment_id,
        question_text='In the 2011 Cricket ODI World Cup quarter-final match between India and Australia, a media organization estimated that Australia would beat India by 50 runs if Australia bats first, based on the information of matches played between the two teams previously. Which branch of statistics does the above analysis belong to?',
        option_a='Descriptive Statistics',
        option_b='Inferential Statistics',
        option_c='Prescriptive Statistics',
        option_d='None of the above',
        correct_option='b'
    )

    question4 = AssignmentQuestion(
        assignment_id=assignment1.assignment_id,
        question_text='Variables with an interval scale of measurement may be converted into a ratio scale of measurement by performing?',
        option_a='Addition',
        option_b='Subtraction',
        option_c='Multiplication',
        option_d='Division',
        correct_option='b'
    )

    question5 = AssignmentQuestion(
        assignment_id=assignment1.assignment_id,
        question_text='What is the scale of measurement for the amount of money you have?',
        option_a='Nominal',
        option_b='Ordinal',
        option_c='Interval',
        option_d='Ratio',
        correct_option='d'
    )

    question6 = AssignmentQuestion(
        assignment_id=assignment1.assignment_id,
        question_text='What is the scale of measurement for the military titles - Major, Captain, Colonel?',
        option_a='Nominal',
        option_b='Ordinal',
        option_c='Interval',
        option_d='Ratio',
        correct_option='b'
    )

    question7 = AssignmentQuestion(
        assignment_id=assignment1.assignment_id,
        question_text='Statement - The sample should be representative of the population.',
        option_a='True, since the sample is a subset of the population.',
        option_b=' True, because the sample is a subset of the population and we derive the properties of the population like mean, median from the sample.',
        option_c='False, sample need not be representative of the population.',
        option_d='None of the above',
        correct_option='b'
    )

    db.session.add_all([question1, question2, question3, question4, question5, question6, question7])
    db.session.commit()

    assignment2 = Assignment(
        course_id='MA1002',
        week_number=2
    )

    db.session.add(assignment2)
    db.session.commit()

    question1 = AssignmentQuestion(
        assignment_id=assignment2.assignment_id,
        question_text='A poll was conducted by IMDb to rank 200 movies released in 2019 based on the revenue collected. Which graph is best suited to represent this data?',
        option_a='Pie Chart',
        option_b='Bar Graph',
        option_c='Pareto Chart',
        option_d='None of the above',
        correct_option='c'
    )

    question2 = AssignmentQuestion(
        assignment_id=assignment2.assignment_id,
        question_text='Which of the following measures of central tendency is applicable for a categorical variable with a nominal scale of measurement?',
        option_a='Mean',
        option_b='Median',
        option_c='Mode',
        option_d='None of the above',
        correct_option='c'
    )

    question3 = AssignmentQuestion(
        assignment_id=assignment2.assignment_id,
        question_text='Identify the wrong statement.',
        option_a='Bar chart is a better tool to describe the Gross Domestic Product (GDP) growth rate of India from 2009 to 2020.',
        option_b='Pie chart is not effective when we have large number of categories.',
        option_c='Pareto chart is used only for ordinal data.',
        option_d='Bar chart is better than pie chart if we want to compare the actual counts.',
        correct_option='c'
    )

    question4 = AssignmentQuestion(
        assignment_id=assignment2.assignment_id,
        question_text='Which of the following is true?',
        option_a='Area principle is only applicable for pie chart not for bar chart.',
        option_b='Rounding off the values of categories leads to misleading of pie chart.',
        option_c='Changing the radius of pie chart leads to loss of information.',
        option_d='Graphs which violate the area principle are called truncated graphs.',
        correct_option='b'
    )

    question5 = AssignmentQuestion(
        assignment_id=assignment2.assignment_id,
        question_text='In order to maximise her profit on sales of mobile phones by buying bulk amount, a seller wishes to analyse the sale numbers of all known brands in the market. Which measure should she use to decide the brands that have been sold in large numbers?',
        option_a='Mean',
        option_b='Median',
        option_c='Mode',
        option_d='None of the above',
        correct_option='c'
    )

    db.session.add_all([question1, question2, question3, question4, question5])
    db.session.commit()

    assignment3 = Assignment(
        course_id='MA1002',
        week_number=3
    )
    db.session.add(assignment3)
    db.session.commit()

    question1 = AssignmentQuestion(
        assignment_id=assignment3.assignment_id,
        question_text='If the sample variance of a data of size 10 is 23, then what is the population variance of this data?',
        option_a='19',
        option_b='20.7',
        option_c='22',
        option_d='23',
        correct_option='b'
    )

    question2 = AssignmentQuestion(
        assignment_id=assignment3.assignment_id,
        question_text='For a particular data, the value for the 10th percentile is 33.5, 25th percentile is 45, 50th percentile is 84.5, and 100th percentile is 102. What is the median of this data?',
        option_a='33.5',
        option_b='45',
        option_c='84.5',
        option_d='102',
        correct_option='c'
    )

    question3 = AssignmentQuestion(
        assignment_id=assignment3.assignment_id,
        question_text='The marks scored by a group of students in an exam is given below.\n\nMarks: 110, 20, 50, 60, 45, 30, 42, 21, 15, 62, 26, 33, 17, 32, 27.\n What is the median of the marks?',
        option_a='39.33',
        option_b='32',
        option_c='33',
        option_d='No median is available for this data',
        correct_option='b'
    )

    question4 = AssignmentQuestion(
        assignment_id=assignment3.assignment_id,
        question_text='The mean of a data is 25 and the standard deviation is 5. What is the coefficient of variation?',
        option_a='0.2',
        option_b='0.25',
        option_c='0.5',
        option_d='0.8',
        correct_option='c'
    )

    question5 = AssignmentQuestion(
        assignment_id=assignment3.assignment_id,
        question_text='If each value of a numerical discrete variable is squared, then the mean of the new data is:',
        option_a='Same as the original mean',
        option_b='Double the original mean',
        option_c='Square of the original mean',
        option_d='Cannot be determined',
        correct_option='d'
    )

    question6 = AssignmentQuestion(
        assignment_id=assignment3.assignment_id,
        question_text='Which of the following is not a measure of dispersion?',
        option_a='Range',
        option_b='Variance',
        option_c='Median',
        option_d='Standard Deviation',
        correct_option='c'
    )

    db.session.add_all([question1, question2, question3, question4, question5, question6])
    db.session.commit()

    assignment4 = Assignment(
        course_id='MA1002',
        week_number=4
    )
    
    db.session.add(assignment4)
    db.session.commit()

    question1 = AssignmentQuestion(
        assignment_id=assignment4.assignment_id,
        question_text='Covariance between two variables is negative when:',
        option_a='Both move in the same direction',
        option_b='Both move in opposite direction',
        option_c='Values taken by both variables is same',
        option_d='The respective difference between both variable values is constant',
        correct_option='b'
    )

    question2 = AssignmentQuestion(
        assignment_id=assignment4.assignment_id,
        question_text='If the correlation coefficient between two variables is 0.8, then:',
        option_a='Both variables are negatively correlated',
        option_b='Both variables are positively correlated',
        option_c='Both variables are not correlated',
        option_d='Cannot be determined',
        correct_option='b'
    )

    question3 = AssignmentQuestion(
        assignment_id=assignment4.assignment_id,
        question_text='Which of the following is not a measure of association?',
        option_a='Covariance',
        option_b='Correlation Coefficient',
        option_c='Coefficient of Determination',
        option_d='Standard Deviation',
        correct_option='d'
    )

    question4 = AssignmentQuestion(
        assignment_id=assignment4.assignment_id,
        question_text='If the sample covariance between X and Y is 45, sample variance of xx is 36 and sample variance of yy is 100, then what is the sample correlation coefficient?',
        option_a='0.55',
        option_b='0.65',
        option_c='0.75',
        option_d='0.85',
        correct_option='c'
    )

    question5 = AssignmentQuestion(
        assignment_id=assignment4.assignment_id,
        question_text='If the slope of the line of best fit is negative, then the correlation between the variables is',
        option_a='Positive',
        option_b='Negative',
        option_c='Zero',
        option_d='Cannot be determined',
        correct_option='b'
    )

    question6 = AssignmentQuestion(
        assignment_id=assignment4.assignment_id,
        question_text='Point Bi-serial correlation coefficient is:',
        option_a='the measure of association between two categorical variables',
        option_b='the measure of association between two numerical variables',
        option_c='the measure of association between numerical and categorical variable',
        option_d='the measure of association between explanatory variable and response variable',
        correct_option='c'
    )

    question7 = AssignmentQuestion(
        assignment_id=assignment4.assignment_id,
        question_text='Let the correlation coefficient r between two variables X and Y be zero. Then, the variables X and Y are:',
        option_a='linearly related',
        option_b='not linearly related',
        option_c='same',
        option_d='none of the above',
        correct_option='b'
    )

    db.session.add_all([question1, question2, question3, question4, question5, question6, question7])
    db.session.commit()

def insert_default_assignments_mlt():
    assignment1 = Assignment(
        course_id='CS2007',
        week_number=1
    )

    db.session.add(assignment1)
    db.session.commit()

    question1 = AssignmentQuestion(
        assignment_id=assignment1.assignment_id,
        question_text='For every mail that comes to your inbox, you have to design an algorithm that can assign exactly one of these four labels to it: family, friends, work, and spam. What type of machine learning problem does this correspond to?',
        option_a='Regression',
        option_b='Binary Classification',
        option_c='Multi-class Classification',
        option_d='This is not a supervised learning problem',
        correct_option='c'
    )

    question2 = AssignmentQuestion(
        assignment_id=assignment1.assignment_id,
        question_text='Which of the following is a supervised learning problem?',
        option_a='Predicting the price of a house given its features',
        option_b='Clustering similar customers together',
        option_c='Finding the most frequent items in a set',
        option_d='All of the above',
        correct_option='a'
    )

    question3 = AssignmentQuestion(
        assignment_id=assignment1.assignment_id,
        question_text='Which of the following is an unsupervised learning problem?',
        option_a='Predicting the price of a house given its features',
        option_b='Clustering similar customers together',
        option_c='Finding the most frequent items in a set',
        option_d='All of the above',
        correct_option='b'
    )

    question4 = AssignmentQuestion(
        assignment_id=assignment1.assignment_id,
        question_text='An image is a collection of pixels. A pixel is stored as a float value and typically occupies 4 bytes of memory. Consider a dataset of 10001000 images, where each image has dimensions 100×100100×100. Approximately, how much memory does the entire dataset occupy?',
        option_a='1 GB',
        option_b='10 GB',
        option_c='100 GB',
        option_d='40 MB',
        correct_option='d'
    )

    question5 = AssignmentQuestion(
        assignment_id=assignment1.assignment_id,
        question_text='What is Principal Component Analysis (PCA) used for?',
        option_a='Feature Selection',
        option_b='Feature Extraction',
        option_c='Dimensionality Reduction',
        option_d='All of the above',
        correct_option='d'
    )

    db.session.add_all([question1, question2, question3, question4, question5])
    db.session.commit()

    assignment2 = Assignment(
        course_id='CS2007',
        week_number=2
    )

    db.session.add(assignment2)
    db.session.commit()

    question1 = AssignmentQuestion(
        assignment_id=assignment2.assignment_id,
        question_text='Which principal component captures the most variance in the dataset?',
        option_a='First Principal Component',
        option_b='Second Principal Component',
        option_c='Last Principal Component',
        option_d='Cannot be determined',
        correct_option='a'
    )

    question2 = AssignmentQuestion(
        assignment_id=assignment2.assignment_id,
        question_text='What will be the time complexity of running PCA using covariance matrix on a dataset containing nn examples in d-dimensional space?',
        option_a='O(n)',
        option_b='O(d)',
        option_c='O(nd)',
        option_d='O(d^3)',
        correct_option='d'
    )

    question3 = AssignmentQuestion(
        assignment_id=assignment2.assignment_id,
        question_text='Consider 100 data points lying uniformly (distances between neighbors are the same) on a circle with the center at the origin. Along which of the following lines, the data points will have the least reconstruction error?',
        option_a='X-axis',
        option_b='Y-axis',
        option_c='Line passing through the origin',
        option_d='Cannot be determined',
        correct_option='d'
    )

    question4 = AssignmentQuestion(
        assignment_id=assignment2.assignment_id,
        question_text='let ϕ be the transformation that maps n d-dimensional data points to D-dimensional data points. What will the covariance matrix shape be in the transformed feature space?',
        option_a='n×n',
        option_b='D×D',
        option_c='n×D',
        option_d='D×n',
        correct_option='b'
    )

    question5 = AssignmentQuestion(
        assignment_id=assignment2.assignment_id,
        question_text='Why finding principal components (eigenvectors) in kernel PCA is not appreciated?',
        option_a='It requires finding the transformation map ϕ and therefore, defeats the purpose of not finding ϕ.',
        option_b='It cannot be calculated as ϕ can never be found.',
        option_c='Principal components in kernel PCA do not capture the variance of the data.',
        option_d='None of the above',
        correct_option='a'
    )

    question6 = AssignmentQuestion(
        assignment_id=assignment2.assignment_id,
        question_text='Which of the following is not a valid kernel function?',
        option_a='Linear Kernel',
        option_b='Polynomial Kernel',
        option_c='Gaussian Kernel',
        option_d='All of the above are valid kernel functions',
        correct_option='d'
    )

    db.session.add_all([question1, question2, question3, question4, question5, question6])
    db.session.commit()

    assignment3 = Assignment(
        course_id='CS2007',
        week_number=3
    )

    db.session.add(assignment3)
    db.session.commit()

    question1 = AssignmentQuestion(
        assignment_id=assignment3.assignment_id,
        question_text='How many configurations are possible for partitioning 100 data points into 10 clusters if these clusters are allowed to be empty?',
        option_a='10^100',
        option_b='100^10',
        option_c='10^10',
        option_d='100×10',
        correct_option='a'
    )

    question2 = AssignmentQuestion(
        assignment_id=assignment3.assignment_id,
        question_text='Which of the following is a clustering algorithm?',
        option_a='K-means',
        option_b='Linear Regression',
        option_c='Logistic Regression',
        option_d='Random Forest',
        correct_option='a'
    )

    question3 = AssignmentQuestion(
        assignment_id=assignment3.assignment_id,
        question_text='A cluster will be good if:',
        option_a='The points in the cluster are far apart.',
        option_b='The points in the cluster are close together.',
        option_c='The points in the cluster are heterogeneous.',
        option_d='The points in the cluster are not similar to each other.',
        correct_option='b'
    )

    question4 = AssignmentQuestion(
        assignment_id=assignment3.assignment_id,
        question_text='Which of the following is a distance metric?',
        option_a='Euclidean Distance',
        option_b='Manhattan Distance',
        option_c='Cosine Similarity',
        option_d='All of the above',
        correct_option='d'
    )

    question5 = AssignmentQuestion(
        assignment_id=assignment3.assignment_id,
        question_text='If μ1 and μ2 are means of two clusters c1 and c2 in k-means, then for all the data points settling in c1:',
        option_a='The means μ1and μ2 are equidistant.',
        option_b='The mean μ2​ is closer than μ1',
        option_c='The mean μ1 is closer than μ2',
        option_d='Insufficient Information.',
        correct_option='c'
    )

    question6 = AssignmentQuestion(
        assignment_id=assignment3.assignment_id,
        question_text='To obtain good clusters, how should the initial means of clusters be?',
        option_a='Means should be as far apart as possible.',
        option_b='Means should be as close to each other as possible.',
        option_c='Means should be randomly initialized.',
        option_d='None of the above',
        correct_option='a'
    )

    question7 = AssignmentQuestion(
        assignment_id=assignment3.assignment_id,
        question_text='Which of the following is correct with respect to the value of k?',
        option_a='The value of k should be as large as possible.',
        option_b='The value of k should be as small as possible.',
        option_c='The value of k should be neither too large nor too small.',
        option_d='The value of k should be randomly initialized.',
        correct_option='c'
    )

    db.session.add_all([question1, question2, question3, question4, question5, question6, question7])
    db.session.commit()
