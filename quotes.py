#python3
#quotes
import random, sys

quotes=[]
quotes.append('The unexamined life is not worth living – Socrates')
quotes.append('Entities should not be multiplied unnecessarily – William of Ockham')
quotes.append('The life of man (in a state of nature) is solitary, poor, nasty, brutish, and short – Thomas Hobbes')
quotes.append('I think, therefore I am (Cogito, ergo sum) – René Descartes')
quotes.append('To be is to be perceived (Esse est percipi)– Bishop George Berkeley')
quotes.append('We live in the best of all possible worlds – Gottfried Wilhelm Leibniz')
quotes.append('What is rational is actual and what is actual is rational – G. W. F. Hegel')
quotes.append('God is dead! He remains dead! And we have killed him. – Friedrich Nietzsche')
quotes.append('There is but one truly serious philosophical problem, and that is suicide – Albert Camus')
quotes.append('One cannot step twice in the same river – Heraclitus')
quotes.append('The greatest happiness of the greatest number is the foundation of morals and legislation – Jeremy Bentham')
quotes.append('Happiness is not an ideal of reason but of imagination – Immanuel Kant')
quotes.append('No man\'s knowledge here can go beyond his experience – John Locke')
quotes.append('God is not willing to do everything, and thus take away our free will and that share of glory which belongs to us – Niccolo Machiavelli')
quotes.append('Liberty consists in doing what one desires – John Stuart Mill')
quotes.append('It is undesirable to believe a proposition when there is no ground whatever for supposing it true – Bertrand Russell')
quotes.append('Even while they teach, men learn – Seneca the Younger')
quotes.append('There is only one good, knowledge, and one evil, ignorance – Socrates')
quotes.append('If God did not exist, it would be necessary to invent Him – Voltaire')
quotes.append('Whoever wishes to become a philosopher must learn not to be frightened by absurdities – Bertrand Russell')
quotes.append('One cannot conceive anything so strange and so implausible that it has not already been said by one philosopher or another – René Descartes')
quotes.append('Leisure is the mother of philosophy – Thomas Hobbes')
quotes.append('Philosophy is a battle against the bewitchment of our intelligence by means of language – Ludwig Wittgenstein')
quotes.append('There is only one thing a philosopher can be relied upon to do, and that is to contradict other philosophers – William James')
quotes.append('We are what we repeatedly do. Excellence, then, is not an act, but a habit – Aristotle')
quotes.append('Life must be understood backward. But it must be lived forward  – Søren Kierkegaard')
quotes.append('Science is what you know. Philosophy is what you don\'t know – Bertrand Russell')
quotes.append('Metaphysics is a dark ocean without shores or lighthouse, strewn with many a philosophic wreck – Immanuel Kant')
quotes.append('Philosophy is at once the most sublime and the most trivial of human pursuits – William James')
quotes.append('History is Philosophy teaching by examples – Thucydides')
quotes.append('He who is unable to live in society, or who has no need because he is sufficient for himself, must be either a beast or a god – Aristotle')
quotes.append('You can discover more about a person in an hour of play than in a year of conversation – Plato')
quotes.append('Things alter for the worse spontaneously, if they be not altered for the better designedly – Francis Bacon')
quotes.append('All that is necessary for the triumph of evil is that good men do nothing – mistakenly attributed to Edmund Burke')
quotes.append('Is man merely a mistake of God\'s? Or God merely a mistake of man\'s? – Friedrich Nietzsche')
quotes.append('I would never die for my beliefs because I might be wrong – Bertrand Russell')
quotes.append('Religion is the sign of the oppressed ... it is the opium of the people – Karl Marx')
quotes.append('Happiness is the highest good – Aristotle')
quotes.append('If men were born free, they would, so long as they remained free, form no conception of good and evil – Baruch Spinoza')
quotes.append('The greater the difficulty, the more glory in surmounting it – Epicurus')
quotes.append('Whatever is reasonable is true, and whatever is true is reasonable – G. W. F. Hegel')
quotes.append('Only one man ever understood me, and he didn\’t understand me – G. W. F. Hegel')
quotes.append('Morality is not the doctrine of how we may make ourselves happy, but of how we may make ourselves worthy of happiness – Immanuel Kant')
quotes.append('Man is condemned to be free – Jean-Paul Sartre')
quotes.append('It is one thing to show a man that he is in error, and another to put him in possession of truth – John Locke')
quotes.append('I don\’t know why we are here, but I’m pretty sure it is not in order to enjoy ourselves – Ludwig Wittgenstein')
quotes.append('That man is wisest who, like Socrates, realizes that his wisdom is worthless – Plato')
quotes.append('The only thing I know is that I know nothing – Socrates')
quotes.append('All is for the best in the best of all possible worlds – Leibniz)')
quotes.append('The function of prayer is not to influence God, but rather to change the nature of the one who prays – Søren Kierkegaard')
quotes.append('Man is born free, but is everywhere in chains – Jean-Jacques Rousseau')
quotes.append('Man will never be free until the last king is strangled with the entrails of the last priest – Denis Diderot')
quotes.append('If you would be a real seeker after truth, it is necessary that at least once in your life you doubt, as far as possible, all things – René Descartes')
quotes.append('Happiness lies in virtuous activity, and perfect happiness lies in the best activity, which is contemplative – Aristotle')
quotes.append('I can control my passions and emotions if I can understand their nature – Baruch Spinoza')
quotes.append('Philosophers have hitherto only interpreted the world in various ways; the point, however, is to change it – Karl Marx')
quotes.append('It is wrong always, everywhere and for everyone, to believe anything upon insufficient evidence – W. K. Clifford')
quotes.append('Virtue is nothing else than right reason – Seneca the Younger')
quotes.append('Freedom is secured not by the fulfilling of one\'s desires, but by the removal of desire – Epictetus')
quotes.append('In everything, there is a share of everything – Anaxagoras')
quotes.append('A little philosophy inclineth man’s mind to atheism; but depth in philosophy bringeth men’s minds about to religion – Sir Francis Bacon')
quotes.append('The brave man is he who overcomes not only his enemies but his pleasures – Democritus')
quotes.append('Good and evil, reward and punishment, are the only motives to a rational creature – John Locke')
quotes.append('To do as one would be done by, and to love one\'s neighbor as oneself, constitute the ideal perfection of utilitarian morality – John Stuart Mill')
quotes.append('Everything that exists is born for no reason, carries on living through weakness, and dies by accident – Jean-Paul Sartre')
quotes.append('Man is the measure of all things – Protagoras')
quotes.append('We are too weak to discover the truth by reason alone – St. Augustine')
quotes.append('The mind is furnished with ideas by experience alone – John Locke')
quotes.append('Whereof one cannot speak, thereof one must be silent – Ludwig Wittgenstein')
quotes.append('He who thinks great thoughts, often makes great errors – Martin Heidegger')

n = random.randint(0,len(quotes) - 1)

#--------------------------translate--------------------------

if len(sys.argv) == 1:
	print(quotes[n])
elif sys.argv[1] == 't':
	import hashlib, bs4, requests, json	
	def makeMD5(transText):
		appKey =                          					#appkey
		salt = '3'                                          #salt
		secretKey =       									#密匙

		hashStr = appKey + transText + salt + secretKey
		sign = hashlib.md5(hashStr.encode(encoding='UTF-8')).hexdigest()
		sign = sign.upper()
		url = 'http://openapi.youdao.com/api?q=' + transText+ '&from=EN&to=zh_CHS&appKey=' + appKey + '&salt=' + salt + '&sign=' + sign
		return url
	def sentenceGetTranslation(transText):
		url = makeMD5(transText)
		res = requests.get(url)
		res.raise_for_status()
		resultList = json.loads(res.content)['translation']
		print(resultList[0])
	sentence = quotes[n]
	try:
		sentenceGetTranslation(sentence)
	except:
		print('出错了')
elif sys.argv[1] == 'h':
	print('quote t to get translate')
else:
	print(quotes[n])