# import pyspark.sql.functions as F
#
# import utils.constants as c
# from transformers.sequence_content_filter_transformer import SequenceContentFilterTransformer
# from pyspark_test import PySparkTest
# from utils.schemas import PLAYLIST_TRACKS_SCHEMA
# from pyspark_commons_test.datasets import get_playlist_metadata
#
#
# class SequenceContentFilterTransformerTest(PySparkTest):
#
#     def test_transform(self):
#         playlists = get_playlist_metadata(self.sc).withColumn(c.TRACK_GROUP, F.col(c.TRACKS).cast(PLAYLIST_TRACKS_SCHEMA))
#         track_category_filters = self.get_track_group_content_filter_table()
#         artist_category_filters = self.get_artist_content_filter_table()
#
#         res = SequenceContentFilterTransformer(track_category_filters,
#                                                artist_category_filters,
#                                                remove_children_music=True,
#                                                remove_ambient_music=True,
#                                                remove_holiday_music=True,
#                                                min_track_streams=500,
#                                                min_track_streamers=200,
#                                                min_track_duration=45,
#                                                max_track_duration=1200,
#                                                min_artist_streams=5_000,
#                                                min_artist_streamers=1_000,
#                                                ).transform(playlists)
#
#         self.assertEqual(3, res.count())
#         self.assertEqual(3, res.select(F.sum(F.size(c.TRACKS)).alias(c.SUM)).collect()[0][c.SUM])
#         self.assertEqual(playlists.schema, res.schema)
#
#     def get_track_group_content_filter_table(self):
#         return self.sc.createDataFrame([
#             ("95476336", True, 300,  10_000, 5_000, 0, 0, 0, 0),
#             ("46882336", True, 300,  100,    20,    0, 0, 0, 0),
#             ("33176280", True, 900,  10_000, 5_000, 0, 0, 0, 0),
#             ("34963569", True, 600,  10_000, 5_000, 0, 0, 0, 0),
#             ("9166747",  True, 300,  10_000, 5_000, 0, 0, 0, 0),
#             ("10251579", True, 300,  10_000, 5_000, 0, 0, 0, 0),
#             ("81728152", True, 300,  10_000, 5_000, 1, 0, 0, 0),
#             ("94401208", True, 300,  10_000, 5_000, 0, 0, 0, 1),
#         ], [c.TRACK_GROUP,
#             c.AVAILABLE,
#             c.DURATION,
#             c.STREAM_COUNT,
#             c.STREAMERS_COUNT,
#             c.CHILDREN,
#             c.HOLIDAY,
#             c.AMBIENT,
#             c.NON_MUSIC])
#
#     def get_artist_content_filter_table(self):
#         return self.sc.createDataFrame([
#             (27446,    True, 100_000, 30_000,  0, 0, 0, 0),
#             (13591,    True, 130_000, 48_000,  0, 0, 0, 0),
#             (3565368,  True, 200,     21,      0, 0, 0, 0),
#             (3565245,  True, 90_000,  11_000,  0, 0, 0, 0),
#             (28481,    True, 80_000,  22_000,  0, 0, 0, 0),
#             (3604413,  True, 220_000, 110_000, 0, 0, 0, 0),
#             (7103647,  True, 20_000,  9_000,   1, 0, 0, 0),
#             (13596,    True, 9_000,   6_000,   0, 0, 0, 1),
#         ], [c.ARTIST_ID, c.AVAILABLE, c.STREAM_COUNT, c.STREAMERS_COUNT, c.CHILDREN, c.AMBIENT, c.HOLIDAY, c.NON_MUSIC])
