# Datasheet: The Artie Bias Corpus

Author: Josh Meyer, PhD

Organization: Artie, Inc.

## Introduction

*The Artie Bias Corpus is a modified subset of the Mozilla Common Voice corpus. All responses and information here is not neccessarily representative of Mozilla or the Common Voice project. We will note when we believe questions are more pertinent to Common Voice than the Artie Bias Corpus. However, we do not claim nor attempt to answer any questions on behalf of Mozilla.*


## Motivation

1. **For what purpose was the dataset created?** Was there a specific task in mind? Was there a specific gap that needed to be filled? Please provide a description.

	*The Artie Bias Corpus was created to detect demographic bias in voice technology applications, specifically automatic speech recognition. There was no such open speech corpus for the English language that could be used with high confidence. Mozilla's Common Voice was the closest applicable corpus, but the labels are crowd-sourced and noisy. Demographic bias is a sensitive topic, and we need data for which we have high confidence in label accuracy.*

2. **Who created this dataset (e.g. which team, research group) and on behalf of which entity (e.g. company, institution, organization)**?

	*The Artie Bias Corpus was curated and annotated by the AI Team at Artie, Inc.*

3. **What support was needed to make this dataset?** (e.g. who funded the creation of the dataset? If there is an associated grant, provide the name of the grantor and the grant name and number, or if it was supported by a company or government agency, give those details.)

	*The Artie Bias Corpus was funded by Artie, Inc., without any outside grants or support.*

4. **Any other comments?**

	*The Artie Bias Corpus is currently English-only, but demographic bias will exist in technologies for all languages. Expanding to new languages is essential.*


## Composition

*Most of these questions are intended to provide dataset consumers with the information they need to make informed decisions about using the dataset for specific tasks.*

1. **What do the instances that comprise the dataset represent (e.g. documents, photos, people, countries)?** Are there multiple types of instances (e.g. movies, users, and ratings; people and interactions between them; nodes and edges)? Please provide a description.

	*The dataset is comprised of MP3 audio recordings of people reading individual sentences or phrases. In addition to the audio, the following are provided in TSV format: an anonymized speaker ID, the text of the sentence which was read in the audio clip, the number of `up votes` and `down votes` from Artie annotators, and self-identified + opt-in demographic data on the speaker of the audio clip `{age, gender, accent}`.*

2. **How many instances are there in total (of each type, if appropriate)?**

	*There are a total of 1,712 audio clips and their accompanying labels.*

3. **Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set?** If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set (e.g. geographic coverage)? If so, please describe how this representativeness was validated/verified. If it is not representative of the larger set, please describe why not (e.g. to cover a more diverse range of instances, because instances were withheld or unavailable).

	*The audio clips in the Artie Bias Corpus are a subset of the test set of the Common Voice corpus released in June 2019 for English. First we subset all audio for which there was at least one demographic label `{age, gender, accent}`, and then re-validated the accuracy of the transcripts. We do not know if the Artie Bias Corpus is a representative subset of the original Common Voice test set, because there were no demographic tags for the rest of the audio.*

4. **What data does each instance consist of?** "Raw" data (e.g. unprocessed text or images) or features? In either case, please provide a description.

	*The audio consists of MP3 files, mono-channel, sampled at 48kHz. The annotations are saved in as raw text in a single TSV file with column headers.*

5. **Is there a label or target associated with each instance?** If so, please provide a description.

	*Each audio clip has the following associated labels: an anonymized speaker ID, the text of the sentence which was read in the audio clip, the number of `up votes` and `down votes` from Artie annotators, and self-identified + opt-in demographic data on the speaker of the audio clip `{age, gender, accent}`.*

6. **Is any information missing from individual instances?** If so, please provide a description, explaining why this information is missing (e.g. because it was unavailable). This does not include intentionally removed information, but might include, e.g. redacted text.

	*Any speaker may have opted to not supply one or more demographic tags. In this case, we have marked the field as `"NA"`.*

7. **Are relationships between individual instances made explicit (e.g. users' movie ratings, social network links)?** If so, please describe how these relationships are made explicit.

	*One speaker may have contributed multiple recordings, and so their anonymized speaker ID will occur in multiple rows of the annotations TSV file.*

8. **Are there recommended data splits (e.g. training, development/validation, testing)?** If so, please provide a description of these splits, explaining the rationale behind them.

	*In it's current format, the Artie Bias Corpus is intended solely as a test set. For most speaker-independent speech applications, the Artie Bias Corpus is too small to be useful as a training set. It may be possible to use as a development as well as a test set, but we have not investigated this and have no recommendations for best practices.*

9. **Are there any errors, sources of noise, or redundancies in the dataset?** If so, please provide a description.

	*There are no errors to our knowledge. Every audio file and associated text transcript has been validated (i.e. voted on) by at least two trained annotators.*

10. **Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g. websites, tweets, other datasets)?** If it links to or relies on external resources, a) are there guarantees that they will exist, and remain constant, over time; b) are there official archival versions of the complete dataset (i.e., including the external resources as they existed at the time the dataset was created); c) are there any restrictions (e.g. licenses, fees) associated with any of the external resources that might apply to a future user? Please provide descriptions of all external resources and any restrictions associated with them, as well as links or other access points, as appropriate.

	*The Artie Bias Corpus is self-contained, and does not rely on any external resources.*

11. **Does the dataset contain data that might be considered confidential (e.g. data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals' non-public communications)?** If so, please provide a description.

	*None of the text read aloud in the corpus is confidential. Contributors read aloud text which has been donated by other users, and presented randomly. There is no relationship between the identity of the speaker and the contents of the text which they read.*

12. **Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety?** If so, please describe why.

	*There is -- to our best judgement -- no content in the Artie Bias Corpus which should be considered offensive, threatening, or might otherwise cause anxiety. During the annotation process we removed one clip from the corpus which may have been considered offensive.*

13. **Does the dataset relate to people?** If not, you may skip the remaining questions in this section.

	*Yes. The data contains human voices and demographic information about the speaker.*

14. **Does the dataset identify any subpopulations (e.g. by age, gender)?** If so, please describe how these subpopulations are identified and provide a description of their respective distributions within the dataset.

	*Yes. The corpus contains self-identified, opt-in tags for age, gender, and accent. The following summary statistics are the distributions by number of audio clips.*

	*Age: 187 Teens, 827 Twenties, 366 Thirties, 152 Fourties, 101 Fifties, 46 Sixties, 18 Seventies, 1 Nineties, 14 NA.*

	*Gender: 257 Female, 1431 Male, 4 Other, 20 NA.*

	*Accent: 24 African, 19 Australia, 10 Bermuda, 42 Canada, 131 England, 10 Hong Kong, 264 Indian, 21 Ireland, 9 Malaysia, 11 New Zealand, 7 Philippines, 12 Scotland, 2 Singapore, 3 South Atlantic, 558 US, 3 Wales, 24 Other, 562 NA.*

15. **Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset?** If so, please describe how.

	*The most information available for any given speaker is their age range (in decades), their gender, and their accent. These three pieces of information do not provide enough precision to identify the speaker without other prior knowledge. As such, the speaker identity may only be identifiable from the audio, and only if the listener already knows the speaker.*

16. **Does the dataset contain data that might be considered sensitive in any way (e.g. data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history)?** If so, please provide a description.

	*The demographic tags {age, accent, gender} may be considered sensitive in nature.*

17. **Any other comments?**

	*Given the un-even distribution of demographic groups in the corpus, statistics for under-represented groups may be less reliable than majority groups. For example, we have only one clip of audio donated by a speaker in their ninties, as such, no real conclusions can be made about speakers in their nineties because no statistics are possible.*


## Collection

*In addition to the goals of the prior section, the answers to questions here may provide information that allow others to reconstruct the dataset without access to it.*

1. **How was the data associated with each instance acquired?** Was the data directly observable (e.g. raw text, movie ratings), reported by subjects (e.g. survey responses), or indirectly inferred/derived from other data (e.g. part-of-speech tags, model-based guesses for age or language)? If data was reported by subjects or indirectly inferred/derived from other data, was the data validated/verified? If so, please describe how.

	*The text sentence was donated, the audio was recorded via the Common Voice platform, the demographic tags were reported by subjects, and the votes were reported by Artie annotators.*

2. **What mechanisms or procedures were used to collect the data (e.g. hardware apparatus or sensor, manual human curation, software program, software API)?** How were these mechanisms or procedures validated?

	*The audio was recorded via the Common Voice platform (web or app-based). Text may have been submitted via Github PRs or the [Sentence Collector](https://common-voice.github.io/sentence-collector/#/).*

3. **If the dataset is a sample from a larger set, what was the sampling strategy (e.g. deterministic, probabilistic with specific sampling probabilities)?**

	*The Artie Bias Corpus is a modified subset of the Common Voice Corpus. All audio containing demographic tags was sampled from the original English release in June 2019. After Artie re-validated this data, we removed 167 clips which did not match their text transcripts. Additionally, we removed 24 clips given other concerns. 22 clips were removed based on concerns that the speakers were not over 18 years old. 1 clip was removed because the user sang the sentence, and 1 clip was removed for problematic content of the text.*

4. **Who was involved in the data collection process (e.g. students, crowdworkers, contractors) and how were they compensated (e.g. how much were crowdworkers paid)?**

	*The speech was donated by crowdsourcing, and speakers were not monitarily compensated.*

5. **Over what timeframe was the data collected?** Does this timeframe match the creation timeframe of the data associated with the instances (e.g. recent crawl of old news articles)? If not, please describe the timeframe in which the data associated with the instances was created. Finally, list when the dataset was first published.

	*We do not know exactly when the audio in the Artie Bias Corpus was donated, but it was gathered from the Common Voice release in June 2019. The Artie Bias Corpus was first released on March 19, 2020.*

7. **Were any ethical review processes conducted (e.g. by an institutional review board)?** If so, please provide a description of these review processes, including the outcomes, as well as a link or other access point to any supporting documentation.

	*The release of the Artie Bias Corpus was reviewed internally on dimensions of (1) potential risk to individuals whose voices are in the corpus, (2) potential risk to demographic groups represented in the corpus, and (3) the intention of individuals who donated their data. Importantly, we evaluated the potential additive effects of inclusion in the Artie Bias Corpus compared to inclusion in Common Voice alone.*

	*We believe that there is minimal additive individual risk of inclusion in the Artie Bias Corpus. Individual risks (such as malicious voice cloning) are not significantly increased by virtue of inclusion in the Artie Bias Corpus. These kinds of risks are present (but minimal) by inclusion in the general Common Voice corpus. We do not believe the Artie Bias Corpus adds any significant individual risk.*

	*With regard to the second point (potential risk to demographic groups), we identified a small additional risk of the Artie Bias Corpus compared to Common Voice alone. This risk is using the data to reach bad conclusions about bias in machine learning applications. This risk would more likely be the result of misguided use than malicious intent. For example, it may be the case that someone without a good understanding of statistical hypothesis testing (e.g. ANOVA tests as used in the Artie Bias Corpus Toolkit) will reach false conclusions using the Artie Bias Corpus, because the tools are easy to use off-the-shelf and will always return a result. The tools return statistical results even when the test should have never been run, because the test itself cannot understand the context of the question. Certain demographics are currently so under-represented in the corpus that no statistical test will return intelligible results. In order to combat this kind of misuse, we made the tools **not** return a simple TRUE/FALSE for detection of bias. Rather the tests return a `p-value` which requires some reading to understand. We do not attempt to digest this information for the user, so that they learn themselves. Furthermore, the user must specify which demographics they are interested in comparing, which avoids so-called ["fishing for p-values"](https://en.wikipedia.org/wiki/Data_dredging).*

	*The third ethical concern relates to the intent of individuals donating to project Common Voice, and whether or not those individuals would approve of hte inclusion of their data in the Artie Bias Corpus. We believe that the goals of releasing the Artie Bias Corpus (openness, fairness, democratization of speech technology) largely align with the intentions individuals may have had when donating to the Common Voice project. Furthermore, when individuals donated their voice data, they did so knowing the data (including their demographic tags) would be released under an open license into the public domain. We continue that tradition, releasing our validation votes into the public domain, and our tools under a permissive license.*

8. **Does the dataset relate to people?** If not, you may skip the remainder of the questions in this section.

	*Yes.*

9. **Did you collect the data from the individuals in question directly, or obtain it via third parties or other sources (e.g. websites)?**

	*We obtained this data from Mozilla's Common Voice release in June 2019.*

10. **Were the individuals in question notified about the data collection?** If so, please describe (or show with screenshots or other information) how notice was provided, and provide a link or other access point to, or otherwise reproduce, the exact language of the notification itself.

	*Individuals were notified about and consented to Mozilla's Common Voice project, and consented to releasing their data into the Public Domain. We do not have exact language of the notification from Mozilla leading up to the June 2019 release. We were not able to notify participants on their specific inclusion in the Artie Bias Corpus.*

11. **Did the individuals in question consent to the collection and use of their data?** If so, please describe (or show with screenshots or other information) how consent was requested and provided, and provide a link or other access point to, or otherwise reproduce, the exact language to which the individuals consented.

	*Individuals were notified about and consented to Mozilla's Common Voice project, and consented to releasing their data into the Public Domain. We do not have exact language of the notification from Mozilla leading up to the June 2019 release. We were not able to notify participants on their specific inclusion in the Artie Bias Corpus.*

12. **If consent was obtained, were the consenting individuals provided with a mechanism to revoke their consent in the future or for certain uses?** If so, please provide a description, as well as a link or other access point to the mechanism (if appropriate).

	*Consent may be revoked by users contacting Mozilla. In such a case, Mozilla should contact all those who downloaded Common Voice, including Artie, Inc. If Artie has been notified that a user present in the Artie Bias Corpus has revoked their consent, that data will be deleted from the corpus.*

13. **Has an analysis of the potential impact of the dataset and its use on data subjects (e.g. a data protection impact analysis) been conducted?** If so, please provide a description of this analysis, including the outcomes, as well as a link or other access point to any supporting documentation.

	*A data protection impact analysis for the release of the Artie Bias Corpus is unnecessary, because it is unlikely to result in a high risk to individuals. Nevertheless, we reviewed DPIA guidelines from the European Commission, and found the Artie Bias Corpus to not pose a high risk to the individuals who donated their data.*

14. **Any other comments?**

	*The data was donated by users under a Creative Commons-0 license into the Public Domain. The Artie Bias Corpus is a specific use-case of this data allowed under the CC0 license. Under these circumstances and in the context of the Common Voice project, we at Artie believe that the potentially sensitive nature of broad demographic tags {age, gender, accent} does not pose a high risk to any of the participants included in the corpus.*


## Preprocessing / Cleaning / Labeling

*The questions in this section are intended to provide dataset consumers with the information they need to determine whether the “raw” data has been processed in ways that are compatible with their chosen tasks. For example, text that has been converted into a “bag-of-words” is not suitable for tasks involving word order.*

1. **Was any preprocessing/cleaning/labeling of the data done (e.g. discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)?** If so, please provide a description. If not, you may skip the remainder of the questions in this section.

	*The text transcripts are original from Mozilla, but we preprocessed our own version to translate digits and other symbols into text. This processed version of the text can be accessed [here](https://github.com/artie-inc/artie-bias-corpus/tree/master/data)*

2. **Was the "raw" data saved in addition to the preprocessed/cleaned/labeled data (e.g. to support unanticipated future uses)?** If so, please provide a link or other access point to the "raw" data.

	*The raw transcripts are supplied by default in the corpus [tarball](http://ml-corpora.artie.com/artie-bias-corpus.tar.gz), but preprocessed transcripts are provided on [Github](https://github.com/artie-inc/artie-bias-corpus/tree/master/data)*

3. **Is the software used to preprocess/clean/label the instances available?** If so, please provide a link or other access point.

	*Data collection and validation was performed via the Common Voice platform, which is open-sourced on [Github](https://github.com/mozilla/voice-web). The modified transcripts on Github (not the default transcripts) were "cleaned" by listening to all audio clips which contained digits or special symbols, and then writing them out in long-form.*

4. **Any other comments?**

	*In summary, we performed our own preprocessing on the text data, but we do not distribute these transcripts by default. If they may be useful, our processed transcripts can be accessed on [Github](https://github.com/artie-inc/artie-bias-corpus/tree/master/data).*


## Uses

*These questions are intended to encourage dataset creators to reflect on the tasks for which the dataset should and should not be used. By explicitly highlighting these tasks, dataset creators can help dataset consumers to make informed decisions, thereby avoiding potential risks or harms.*

1. **Has the dataset been used for any tasks already?** If so, please provide a description.

	*The Artie Bias Corpus has been used to detect gender and accent bias in Google, Amazon, and Mozilla's automatic speech recognition software, as reported [here](https://www.artie.com/blog/the-artie-bias-corpus).*

2. **Is there a repository that links to any or all papers or systems that use the dataset?** If so, please provide a link or other access point.

	*Yes. There is a list of publications on [Github](https://github.com/artie-inc/artie-bias-corpus/blob/master/PUBLICATIONS.md), which is maintained by Artie, Inc..*

3. **What (other) tasks could the dataset be used for?**

	*Bias detection in other speech applications such as speaker recognition, voice activity detection, key word spotting.*

4. **Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?** For example, is there anything that a future user might need to know to avoid uses that could result in unfair treatment of individuals or groups (e.g. stereotyping, quality of service issues) or other undesirable harms (e.g. financial harms, legal risks) If so, please provide a description. Is there anything a future user could do to mitigate these undesirable harms?

	*Currently, the demographics of the Artie Bias Corpus are not evenly distributed. This means that the corpus may fail to detect bias in some applications due to lack of statistical power, not because a bias doesn't exist. For example, the corpus may not be useful for detecting a gender bias in software which actually does have a gender bias because there are not enough recordings of female voices.*

5. **Are there tasks for which the dataset should not be used?** If so, please provide a description.

	*The data should not be used to identify the individuals who recorded the data. The data should not be used in any way that would bring harm to any of the demographic groups present in the data.*

6. **Any other comments?**

	*The Artie Bias Corpus was designed for and should be used for improving speech technologies for under-represented demographics. It should not be used in any way for discrimination or to harm the speakers or groups represented in the corpus.*


## Distribution

1. **Will the dataset be distributed to third parties outside of the entity (e.g. company, institution, organization) on behalf of which the dataset was created?** If so, please provide a description.

	*Yes. The Artie Bias Corpus is freely available for download and released under a Creative Commons-0 license.*

2. **How will the dataset will be distributed (e.g. tarball on website, API, GitHub)?** Does the dataset have a digital object identifier (DOI)?

	*The Artie Bias Corpus is distributed as a [tarball](http://ml-corpora.artie.com/artie-bias-corpus.tar.gz), hosted by Artie, Inc.*

3. **When will the dataset be distributed?**

	*The corpus was first released on March 19, 2020, and is available as a tarball at the stable link here <http://ml-corpora.artie.com/artie-bias-corpus.tar.gz>.*

4. **Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)?** If so, please describe this license and/or ToU, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms or ToU, as well as any fees associated with these restrictions.

	*The Artie Bias Corpus is released under a [Creative Commons-0 license](https://creativecommons.org/publicdomain/zero/1.0/).*
	
	<a rel="license" href="https://creativecommons.org/publicdomain/zero/1.0/"><img alt="Creative Commons License" style="border-width:0" src="https://licensebuttons.net/l/zero/1.0/88x31.png" /></a>

5. **Have any third parties imposed IP-based or other restrictions on the data associated with the instances?** If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms, as well as any fees associated with these restrictions.

	*No.*

6. **Do any export controls or other regulatory restrictions apply to the dataset or to individual instances?** If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any supporting documentation.

	*No.*

7. **Any other comments?**

	*The current download size of the tarball is 63.9MB.*


## Maintenance

1. **Who is supporting/hosting/maintaining the dataset?**

	*Artie, Inc.*

2. **How can the owner/curator/manager of the dataset be contacted (e.g. email address)?**

	*Via email at <info@artie.com>*

3. **Is there an erratum?** If so, please provide a link or other access point.

	*No. However, any changes in the data will be recorded and released with the current download, and the Github repo may contain information in the changelogs.*

4. **Will the dataset be updated (e.g. to correct labeling errors, add new instances, delete instances)?** If so, please describe how often, by whom, and how updates will be communicated to users (e.g. mailing list, GitHub)?

	*There are no current plans to add new instances. However, we welcome contributions. If we receive new contributions, we will make the newer corpus downloadable from the current tarball link. Within the download will be information about versions of the data.*

5. **If the dataset relates to people, are there applicable limits on the retention of the data associated with the instances (e.g. were individuals in question told that their data would be retained for a fixed period of time and then deleted)?** If so, please describe these limits and explain how they will be enforced.

	*There are no retention limits for this data.*

6. **Will older versions of the dataset continue to be supported/hosted/maintained?** If so, please describe how. If not, please describe how its obsolescence will be communicated to users.

	*In the case of an update, older versions of the Artie Bias Corpus will continue to be maintained and available for download as tarballs. Any list of releases will exist in the Github repo.*

7. **If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so?** If so, please provide a description. Will these contributions be validated/verified? If so, please describe how. If not, why not? Is there a process for communicating/distributing these contributions to other users? If so, please provide a description.

	*If others would like to contribute to the Artie Bias Corpus, you should validate more audio from Common Voice with trained annotators. You can validate data from any of the train/dev/test sets, because they are not guaranteed to carry over from release to release. You should use the same data annotation guide we developed and used [here](https://github.com/artie-inc/artie-bias-corpus/blob/master/misc/ANNOTATION_GUIDE.md). If you have changes to propose or discussion about the annotation guide, please submit a Pull Request or open an Issue on the repo. Importantly, new contributions should focus on adding more data to demographics which are currently under-represented in the corpus.*

8. **Any other comments?**

	*No.*
