# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Album'
        db.create_table('pwadio_be_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('year_released', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pwadio_be.Artist'])),
            ('CDDB_ID', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('AllMusic_ID', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('FreeDB_ID', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('iTunes_ID', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('pwadio_be', ['Album'])

        # Adding model 'processing_Time'
        db.create_table('pwadio_be_processing_time', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station_ID', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pwadio_be.radio_station'])),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('download_site_time', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=5)),
            ('processing_time', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=5)),
            ('total_elapsed_time', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=5)),
            ('number_of_tracks_added_this_batch', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('pwadio_be', ['processing_Time'])

        # Adding model 'running_playlist'
        db.create_table('pwadio_be_running_playlist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Unique_ID', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('time_played', self.gf('django.db.models.fields.DateTimeField')()),
            ('radio_station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pwadio_be.radio_station'])),
            ('artist_name_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('track_name_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('artist', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('track', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('pwadio_be', ['running_playlist'])

        # Adding model 'Artist'
        db.create_table('pwadio_be_artist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('URL', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('CDDB_ID', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('AllMusic_ID', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('FreeDB_ID', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('iTunes_ID', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('pwadio_be', ['Artist'])

        # Adding model 'Track'
        db.create_table('pwadio_be_track', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('year_released', self.gf('django.db.models.fields.DateTimeField')()),
            ('track_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pwadio_be.Artist'])),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pwadio_be.Album'])),
            ('CDDB_ID', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('AllMusic_ID', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('FreeDB_ID', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('iTunes_ID', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('pwadio_be', ['Track'])

        # Adding model 'radio_station'
        db.create_table('pwadio_be_radio_station', (
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
        db.send_create_signal('pwadio_be', ['radio_station'])

        # Adding model 'LibraryConnection'
        db.create_table('pwadio_be_libraryconnection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('URL', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('search_API_URL', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('search_URL', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('developer_ID', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=600)),
        ))
        db.send_create_signal('pwadio_be', ['LibraryConnection'])

        # Adding model 'iTunes_track_info'
        db.create_table('pwadio_be_itunes_track_info', (
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
        db.send_create_signal('pwadio_be', ['iTunes_track_info'])


    def backwards(self, orm):
        # Deleting model 'Album'
        db.delete_table('pwadio_be_album')

        # Deleting model 'processing_Time'
        db.delete_table('pwadio_be_processing_time')

        # Deleting model 'running_playlist'
        db.delete_table('pwadio_be_running_playlist')

        # Deleting model 'Artist'
        db.delete_table('pwadio_be_artist')

        # Deleting model 'Track'
        db.delete_table('pwadio_be_track')

        # Deleting model 'radio_station'
        db.delete_table('pwadio_be_radio_station')

        # Deleting model 'LibraryConnection'
        db.delete_table('pwadio_be_libraryconnection')

        # Deleting model 'iTunes_track_info'
        db.delete_table('pwadio_be_itunes_track_info')


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
        'pwadio_be.itunes_track_info': {
            'Meta': {'object_name': 'iTunes_track_info'},
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
        'pwadio_be.processing_time': {
            'Meta': {'object_name': 'processing_Time'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'download_site_time': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_tracks_added_this_batch': ('django.db.models.fields.IntegerField', [], {}),
            'processing_time': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '5'}),
            'station_ID': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pwadio_be.radio_station']"}),
            'total_elapsed_time': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '5'})
        },
        'pwadio_be.radio_station': {
            'Meta': {'object_name': 'radio_station'},
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
        'pwadio_be.running_playlist': {
            'Meta': {'object_name': 'running_playlist'},
            'Unique_ID': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'artist_name_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'radio_station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pwadio_be.radio_station']"}),
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