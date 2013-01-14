# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'ItunesTrackInfo', fields ['artist_id']
        db.delete_unique('pwadio_be_2_itunestrackinfo', ['artist_id'])


    def backwards(self, orm):
        # Adding unique constraint on 'ItunesTrackInfo', fields ['artist_id']
        db.create_unique('pwadio_be_2_itunestrackinfo', ['artist_id'])


    models = {
        'pwadio_be_2.album': {
            'Meta': {'object_name': 'Album'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pwadio_be_2.Artist']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'year_released': ('django.db.models.fields.DateTimeField', [], {})
        },
        'pwadio_be_2.artist': {
            'Meta': {'object_name': 'Artist'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'pwadio_be_2.itunestrackinfo': {
            'Meta': {'object_name': 'ItunesTrackInfo'},
            'artist_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'artist_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'artist_view_URL': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'artwork_URL_100': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'artwork_URL_30': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'artwork_URL_60': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'collection_Id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'collection_censored_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'collection_explicitness': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'collection_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'collection_price': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'collection_view_URL': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'content_advisory_rating': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'disc_count': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'disc_number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'long_description': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'preview_URL': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'primary_genre_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'release_date': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'track_censored_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'track_count': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'track_explicitness': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'track_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'track_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'track_number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'track_price': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'track_time_millis': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'track_view_URL': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'wrapper_type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'pwadio_be_2.musicservices': {
            'Meta': {'object_name': 'MusicServices'},
            'URL': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'apiURL': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'developer_ID': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'search_API_URL': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'search_URL': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'pwadio_be_2.musicservices_artist_lookup': {
            'Meta': {'object_name': 'MusicServices_Artist_Lookup'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['pwadio_be_2.Artist']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'music_service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['pwadio_be_2.MusicServices']"}),
            'music_service_object_id_from_web': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'pwadio_be_2.musicservices_track_lookup': {
            'Meta': {'object_name': 'MusicServices_Track_Lookup'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'music_service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['pwadio_be_2.MusicServices']"}),
            'music_service_object_id_from_web': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'track': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['pwadio_be_2.Track']"})
        },
        'pwadio_be_2.processingtime': {
            'Meta': {'object_name': 'ProcessingTime'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'download_site_time': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '5'}),
            'finish_reason': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
            'finish_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_tracks_added_this_batch': ('django.db.models.fields.IntegerField', [], {}),
            'processing_time': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '5'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'station_ID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pwadio_be_2.RadioStation']"}),
            'total_elapsed_time': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '5'})
        },
        'pwadio_be_2.radiostation': {
            'Meta': {'object_name': 'RadioStation'},
            'URL': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'am_fm_band': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone_1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone_2': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'playlist_URL': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'pwadio_be_2.runningplaylist': {
            'Meta': {'object_name': 'RunningPlaylist'},
            'Unique_ID': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pwadio_be_2.Artist']"}),
            'artist_name_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'processing_time': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pwadio_be_2.ProcessingTime']"}),
            'radio_station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pwadio_be_2.RadioStation']"}),
            'time_played': ('django.db.models.fields.DateTimeField', [], {}),
            'track': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pwadio_be_2.Track']"}),
            'track_name_text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'pwadio_be_2.track': {
            'Meta': {'object_name': 'Track'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pwadio_be_2.Artist']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['pwadio_be_2']