from pydub import AudioSegment


podcastSeg = AudioSegment.from_file("AudioFiles/PodcastClip.mp3", "mp3")
introSeg = AudioSegment.from_file("AudioFiles/Intro.mp3", "mp3")
outroSeg = AudioSegment.from_file("AudioFiles/Intro.mp3", "mp3")
interstitialSeg = AudioSegment.from_file("AudioFiles/Intro.mp3", "mp3")



# pydub does things in milliseconds

first_5_secs = podcastSeg[:5000]
last_5_secs = podcastSeg[-5000:]

fadeInOutSeg = introSeg.append(podcastSeg, crossfade=1500).append(outroSeg, crossfade=1500)

fadeInOutSeg.export("OutputAudioFiles/fadeInOutSeg.mp3", format="mp3")

timeSplit = 30 * 1000
podcastFirstSeg = podcastSeg[:timeSplit]
podcastSecondSeg = podcastSeg[-timeSplit:]

fadeInOutWithInterstitialSeg = introSeg.append(podcastFirstSeg, crossfade=1500)\
                                .append(interstitialSeg, crossfade=1500)\
                                .append(podcastSecondSeg, crossfade=1500)\
                                .append(outroSeg, crossfade=1500)
fadeInOutWithInterstitialSeg.export("OutputAudioFiles/fadeInOutInterstitialSeg.mp3", format="mp3")




# # reduce volume by 6dB
# beginning = first_5_secs - 3
#
# # reduce volume by 3dB
# end = last_5_secs - 3
#
#
# begin_end = beginning + end
#
# export = begin_end.export("OutputAudioFiles/test.mp3", format="mp3")

# awesome = podcastSeg.fade_in(2000).fade_out(3000)
#
# awesome.export("mashup.mp3", format="mp3")