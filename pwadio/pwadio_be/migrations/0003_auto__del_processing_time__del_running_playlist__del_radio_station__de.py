# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'processing_Time'
        db.delete_table('pwadio_be_processing_time')

        # Deleting model 'running_playlist'
        db.delete_table('pwadio_be_running_playlist')

        # Deleting model 'radio_station'
        db.delete_table('pwadio_be_radio_station')

        # Deleting model 'iTunes_track_info'
        db.delete_table('pwadio_be_itunes_track_info')

        # Adding model 'ProcessingTime'
        db.create_table('pwadio_be_processingtime', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station_ID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pwadio_be.RadioStation'])),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('download_site_time', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=5)),
            ('processing_time', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=5)),
            ('total_elapsed_time', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=5)),
            ('number_of_tracks_added_this_batch', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('pwadio_be', ['ProcessingTime'])

        # Adding model 'RunningPlaylist'
        db.create_table('pwadio_be_runningplaylist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Unique_ID', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('time_played', self.gf('django.db.models.fields.DateTimeField')()),
            ('radio_station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pwadio_be.RadioStation'])),
            ('artist_name_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('track_name_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('artist', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('track', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('pwadio_be', ['RunningPlaylist'])

        # Adding model 'RadioStation'
        db.create_table('pwadio_be_radiostation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('URL', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('playlist_URL', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('am_fm_band', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('frequency', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phone_1', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phone_2', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=600)),
        ))
        db.send_create_signal('pwadio_be', ['RadioStation'])

        # Adding model 'ItunesTrackInfo'
        db.create_table('pwadio_be_itunestrackinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('wrapper_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('artist_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('collection_Id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('track_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('artist_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('collection_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('track_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('collection_censored_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('track_censored_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('artist_view_URL', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('collection_view_URL', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('track_view_URL', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('preview_URL', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('artwork_URL_30', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('artwork_URL_60', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('artwork_URL_100', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('collection_price', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('track_price', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('release_date', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('collection_explicitness', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('track_explicitness', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('disc_count', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('disc_number', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('track_count', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('track_number', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('track_time_millis', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('primary_genre_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('content_advisory_rating', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('long_description', self.gf('django.db.models.fields.CharField')(max_length=400)),
        ))
        db.send_create_signal('pwadio_be', ['ItunesTrackInfo'])


    def backwards(self, orm):
        # Adding model 'processing_Time'
        db.create_table('pwadio_be_processing_time', (
            ('download_site_time', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=5)),
            ('number_of_tracks_added_this_batch', self.gf('django.db.models.fields.IntegerField')()),
            ('processing_time', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=5)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station_ID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pwadio_be.radio_station'])),
            ('total_elapsed_time', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=5)),
        ))
        db.send_create_signal('pwadio_be', ['processing_Time'])

        # Adding model 'running_playlist'
        db.create_table('pwadio_be_running_playlist', (
            ('time_played', self.gf('django.db.models.fields.DateTimeField')()),
            ('radio_station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pwadio_be.radio_station'])),
            ('track_name_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('artist', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('track', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('artist_name_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Unique_ID', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('pwadio_be', ['running_playlist'])

        # Adding model 'radio_station'
        db.create_table('pwadio_be_radio_station', (
            ('am_fm_band', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('URL', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('playlist_URL', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('frequency', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('phone_2', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone_1', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('pwadio_be', ['radio_station'])

        # Adding model 'iTunes_track_info'
        db.create_table('pwadio_be_itunes_track_info', (
            ('wrapper_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('primary_genre_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('track_time_millis', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('track_view_URL', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('collection_censored_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('artwork_URL_60', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('collection_price', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('track_price', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('preview_URL', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('artist_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('artist_view_URL', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('artwork_URL_30', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('track_explicitness', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('track_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_advisory_rating', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('collection_view_URL', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('track_number', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('artwork_URL_100', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('track_count', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('disc_count', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('collection_explicitness', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('release_date', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('long_description', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('disc_number', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('collection_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('collection_Id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('artist_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('track_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('track_censored_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('pwadio_be', ['iTunes_track_info'])

        # Deleting model 'ProcessingTime'
        db.delete_table('pwadio_be_processingtime')

        # Deleting model 'RunningPlaylist'
        db.delete_table('pwadio_be_runningplaylist')

        # Deleting model 'RadioStation'
        db.delete_table('pwadio_be_radiostation')

        # Deleting model 'ItunesTrackInfo'
        db.delete_table('pwadio_be_itunestrackinfo')


    models = {
        'pwadio_be.album': {
            'AllMusic_ID': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'CDDB_ID': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'FreeDB_ID': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Meta': {'object_name': 'Album'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pwadio_be.Artist']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'iTunes_ID': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'year_released': ('django.db.models.fields.DateTimeField', [], {})
        },
        'pwadio_be.artist': {
            'AllMusic_ID': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'CDDB_ID': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'FreeDB_ID': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Meta': {'object_name': 'Artist'},
            'URL': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'iTunes_ID': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'pwadio_be.itunestrackinfo': {
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
            'track_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'track_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'track_number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'track_price': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'track_time_millis': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'track_view_URL': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'wrapper_type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'pwadio_be.libraryconnection': {
            'Meta': {'object_name': 'LibraryConnection'},
            'URL': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'developer_ID': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'search_API_URL': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'search_URL': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'pwadio_be.processingtime': {
            'Meta': {'object_name': 'ProcessingTime'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'download_site_time': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_tracks_added_this_batch': ('django.db.models.fields.IntegerField', [], {}),
            'processing_time': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '5'}),
            'station_ID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pwadio_be.RadioStation']"}),
            'total_elapsed_time': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '5'})
        },
        'pwadio_be.radiostation': {
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
        'pwadio_be.runningplaylist': {
            'Meta': {'object_name': 'RunningPlaylist'},
            'Unique_ID': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'artist_name_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'radio_station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pwadio_be.RadioStation']"}),
            'time_played': ('django.db.models.fields.DateTimeField', [], {}),
            'track': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'track_name_text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'pwadio_be.track': {
            'AllMusic_ID': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'CDDB_ID': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'FreeDB_ID': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Meta': {'object_name': 'Track'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pwadio_be.Album']"}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pwadio_be.Artist']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'iTunes_ID': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'track_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'year_released': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['pwadio_be']