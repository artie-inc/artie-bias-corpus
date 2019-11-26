# Validation Criteria

The following are written notes that were used by the Artie annotators when validating the Artie Bias Corpus.

## General

We will be using this data set to judge the performance of a speech recognition system. If the ASR system were to perform a perfect transcription (i.e. transcribes every spoken word in the audio accurately), would that transcription match the text on the screen? If not, then REJECT the <text, audio> pair, otherwise, ACCEPT the pair.

## YES == the text and the audio match exactly
## NO == the transcript and the words spoken do not match exactly

### Children

There are children in this dataset. When you hear what you think is a child, please make note. We will remove the sentences before release.

## Specific Examples:

- If there is background talking, this is OK as long as that background talking is unintelligible… if you can make out *any* words in the background speech, then you should REJECT
- Feel free to replay sentences
- Listen to the entire audio clip -- sometimes there are extra words at the very end.
- If the clip is so quiet that you can barely hear it with headphones on full volume, then REJECT
- Pay special attention to things like “we’re” vs “we are”. Many speakers get this wrong or inadvertently shorten words when speaking quickly, e.g. “gonna” instead of “going to”.
- When it comes to accents, there can be some grey areas in terms of pronunciation. I tend to give a fair amount of leeway and base it on whether I could understand the sentence if spoken to me, but I reject if the pronunciation makes it sound too much like a different word.
- Ultimately a lot of it is up to your own discretion. If in doubt, REJECT. There’s plenty of other recordings and we would rather have a slightly smaller, but higher quality corpus.
- Whispering is OK if intelligible
- Carefully listen to native speakers with accents unfamiliar to you (e.g. Indian, UK, Australian). You should only reject if there is a real error, not just because the accent is different from yours!
- Replacing similar words is a REJECT (e.g. saying “a” instead of “the”)
- Skipping words is a REJECT (e.g. “the” gets skipped frequently)
- If the mis-pronunciation is severe enough to be a different word (e.g. “she” is pronounced as “sea” or “seize” as “size”) REJECT
- If the mispronunciation does not result in a different word that exists in English, and it could be understood given knowledge of the accent, ACCEPT (“vandalism” said like “wandalism” is OK)
