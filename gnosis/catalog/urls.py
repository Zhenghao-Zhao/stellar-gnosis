from django.urls import path
from . import views
from bookmark.views import *  #bookmark_entry_remove, bookmark_entry_remove_from_view

urlpatterns = [
    path('', views.papers),
    path('papers/', views.papers, name='papers_index'),
    path('persons/', views.persons, name='persons_index'),
    path('paper/<int:id>/', views.paper_detail, name='paper_detail'),
    path('build', views.build, name='build_db'),
]

# for updating/creating a new Paper node
urlpatterns += [
    path('paper/<int:id>/update', views.paper_update, name='paper_update'),
    path('paper/<int:id>/delete', views.paper_delete, name='paper_delete'),
    path('paper/<int:id>/connect/venue', views.paper_connect_venue, name='paper_connect_venue'),
    path('paper/<int:id>/connect/venue/<int:vid>', views.paper_connect_venue_selected, name='paper_connect_venue_selected'),
    path('paper/<int:id>/connect/author', views.paper_connect_author, name='paper_connect_author'),
    path('paper/<int:id>/connect/author/<int:aid>', views.paper_connect_author_selected, name='paper_connect_author_selected'),
    path('paper/<int:id>/connect/paper', views.paper_connect_paper, name='paper_connect_paper'),
    path('paper/<int:id>/connect/paper/<int:pid>', views.paper_connect_paper_selected, name='paper_connect_paper_selected'),
    path('paper/<int:id>/connect/dataset', views.paper_connect_dataset, name='paper_connect_dataset'),
    path('paper/<int:id>/connect/dataset/<int:did>', views.paper_connect_dataset_selected, name='paper_connect_dataset_selected'),
    path('paper/<int:id>/connect/code', views.paper_connect_code, name='paper_connect_code'),
    path('paper/<int:id>/connect/code/<int:cid>', views.paper_connect_code_selected, name='paper_connect_code_selected'),
    path('paper/<int:id>/authors', views.paper_authors, name='paper_authors'),
    path('paper/<int:id>/remove/author/<int:rid>', views.paper_remove_author, name='paper_remove_author'),
    path('paper/create/', views.paper_create, name='paper_create'),
    path('paper/import/', views.paper_create_from_url, name='paper_create_from_url'),
    path('paper/find/', views.paper_find, name='paper_find'),
    path('paper/<int:id>/group/add', views.paper_add_to_group, name='paper_add_to_group'),
    path('paper/<int:id>/group/add/<int:gid>', views.paper_add_to_group_selected, name='paper_add_to_group_selected'),
    path('paper/<int:id>/collection/add', views.paper_add_to_collection, name='paper_add_to_collection'),
    path('paper/<int:id>/collection/add/<int:cid>', views.paper_add_to_collection_selected, name='paper_add_to_collection_selected'),
    path('paper/<int:id>/bookmark', views.paper_bookmark, name='paper_bookmark'),
    path('paper/<int:id>/add/note/', views.paper_add_note, name='paper_add_note'),
    path('paper/<int:id>/comment/<int:cid>/flag', views.paper_flag_comment, name='paper_flag_comment'),
]

# for updating/creating a new Person node
urlpatterns += [
    path('person/create/', views.person_create, name='person_create'),
    path('person/<int:id>/', views.person_detail, name='person_detail'),
    path('person/<int:id>/update', views.person_update, name='person_update'),
    path('person/<int:id>/delete', views.person_delete, name='person_delete'),
    # path('person/find/', views.person_find, name='person_find'),
]

# for updating/creating a new Dataset node
urlpatterns += [
    path('datasets/', views.datasets, name='datasets_index'),
    path('dataset/create/', views.dataset_create, name='dataset_create'),
    # path('dataset/find/', views.dataset_find, name='dataset_find'),
    path('dataset/<int:id>/', views.dataset_detail, name='dataset_detail'),
    path('dataset/<int:id>/update', views.dataset_update, name='dataset_update'),
    path('dataset/<int:id>/delete', views.dataset_delete, name='dataset_delete'),
]

# for updating/creating a new Venue node
urlpatterns += [
    path('venues/', views.venues, name='venues_index'),
    path('venue/create/', views.venue_create, name='venue_create'),
    path('venue/find/', views.venue_find, name='venue_find'),
    path('venue/<int:id>/', views.venue_detail, name='venue_detail'),
    path('venue/<int:id>/update', views.venue_update, name='venue_update'),
    path('venue/<int:id>/delete', views.venue_delete, name='venue_delete'),
]


# for updating/creating a new Comment node
urlpatterns += [
    path('comments/', views.comments, name='comments_index'),
    path('comment/<int:id>/', views.comment_detail, name='comment_detail'),
    path('comment/<int:id>/update', views.comment_update, name='comment_update'),
    path('comment/<int:id>/delete', views.comment_delete, name='comment_delete'),
    path('comment/<int:id>/restore', views.comment_restore, name='comment_restore'),
    path('flaggedcomments/', views.flagged_comments, name='flagged_comments_index'),
]

# for updating/creating a new Code node
urlpatterns += [
    path('codes/', views.codes, name='codes_index'),
    path('code/create/', views.code_create, name='code_create'),
    path('code/find/', views.code_find, name='code_find'),
    path('code/<int:id>/', views.code_detail, name='code_detail'),
    path('code/<int:id>/update', views.code_update, name='code_update'),
    path('code/<int:id>/delete', views.code_delete, name='code_delete'),
]

# for updating/creating a ReadingGroup object
urlpatterns += [
    path('groups', views.groups, name='groups_index'),
    path('group/create/', views.group_create, name='group_create'),
    path('group/<int:id>', views.group_detail, name='group_detail'),
    path('group/<int:id>/update', views.group_update, name='group_update'),
    path('group/<int:id>/join', views.group_join, name='group_join'),
    path('group/<int:id>/leave', views.group_leave, name='group_leave'),
    path('group/<int:id>/managemembers', views.group_manage_members, name='group_manage_members'),
    path('group/<int:id>/delete', views.group_delete, name='group_delete'),
    path('group/<int:id>/entry/<int:eid>/update', views.group_entry_update, name='group_entry_update'),
    path('group/<int:id>/entry/<int:eid>/remove', views.group_entry_remove, name='group_entry_remove'),
    path('group/<int:id>/entry/<int:eid>/unschedule', views.group_entry_unschedule, name='group_entry_unschedule'),
    path('group/<int:id>/user/<int:aid>/grant', views.group_grant_access, name='group_grant_access'),
    path('group/<int:id>/user/<int:aid>/deny', views.group_deny_access, name='group_deny_access'),
]

# for updating/creating a Collection
urlpatterns += [
    path('collections', views.collections, name='collections'),
    path('collection/create/', views.collection_create, name='collection_create'),
    path('collection/<int:id>', views.collection_detail, name='collection_detail'),
    path('collection/<int:id>/update', views.collection_update, name='collection_update'),
    path('collection/<int:id>/delete', views.collection_delete, name='collection_delete'),
    path('collection/<int:id>/entry/<int:eid>/remove', views.collection_entry_remove, name='collection_entry_remove'),
]

# for updating/creating a Endorsement
urlpatterns += [
    path('endorsements/', views.endorsements, name='endorsements'),
    path('endorsements/search/', views.endorsement_search, name='endorsement_search'),
    path('endorsements/create/<int:id>', views.endorsement_create, name='endorsement_create'),
    path('endorsements/delete/<int:id>', views.endorsement_delete, name='endorsement_delete'),
]

# for updating/creating a user's Profile
urlpatterns += [
    path('profile/<int:id>', views.profile_detail, name='profile'),
    path('profile/update', views.profile_update, name='profile_update'),
]


# for updating/creating a Bookmark
urlpatterns += [
    # path('bookmarks/entry/<int:pid>', views.paper_add_to_bookmark, name='paper_add_to_bookmark'),
    # path('bookmarks/paper/<int:pid>/remove', bookmark_entry_remove, name='bookmark_entry_remove'),
    # path('bookmarks/<int:pid>/remove', bookmark_entry_remove_from_view, name='bookmark_entry_remove_from_view'),

]

urlpatterns += [
    path('flags/comment/<int:comment_id>/create', views.cflag_create, name='comment_flag_create'),
    path('flags/comment/<int:comment_id>/remove', views.cflag_remove, name='comment_flag_remove'),
]
