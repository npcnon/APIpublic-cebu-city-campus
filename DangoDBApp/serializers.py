# DangoDBApp.serializers

from datetime import datetime, date
import re
from rest_framework import serializers
from .models import (
    TblRoomInfo,
    TblProgram,
    TblDepartment,
    TblUsers,
    TblStudentPersonalData,
    TblStudentFamilyBackground,
    TblStudentAcademicBackground,
    TblStudentAcademicHistory,
    TblStudentAddPersonalData,
    TblStudentBasicInfo,
    TblBugReport,
    TblStudentOfficialInfo,
)

# Generalized DateField that handles date parsing/validation
class TblStudentOfficialInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblStudentOfficialInfo
        fields = '__all__'
    def validate_student_id(self, value):
        # Validate format
        if not re.match(r'^\d{4}-\d{5}$', value):
            raise serializers.ValidationError('Student ID must be in the format YYYY-NNNNN, where YYYY is the year, and NNNNN is the student number (5 digits).')
        return value

    def validate(self, data):

        student_id = data.get('student_id')
        if student_id:
            parts = student_id.split('-')
            if len(parts) == 2:
                year, number = parts
                normalized_student_id = f"{year}-{number}"
                data['student_id'] = normalized_student_id
            else:
                raise serializers.ValidationError('Student ID must be in the format YYYY-NNNNN.')
        return data



class CustomDateField(serializers.DateField):
    def to_internal_value(self, value):
        if isinstance(value, str):
            try:
                return datetime.strptime(value, '%Y-%m-%d').date()
            except ValueError:
                raise serializers.ValidationError("Date has wrong format. Use YYYY-MM-DD.")
        elif isinstance(value, date):
            return value
        else:
            raise serializers.ValidationError("Invalid date format.")

def create_serializer(model_class):
    class ModelSerializer(serializers.ModelSerializer):
        # Generalized date fields processing
        def get_fields(self):
            fields = super().get_fields()
            for field_name, field in fields.items():
                if isinstance(field, serializers.DateField):
                    fields[field_name] = CustomDateField(input_formats=['%Y-%m-%d'])
            return fields

        class Meta:
            model = model_class
            fields = '__all__'
    
    return ModelSerializer



def create_fullstudentdata_serializer(model_class):
    class ModelSerializer(serializers.ModelSerializer):
        fulldata_applicant_id = serializers.PrimaryKeyRelatedField(read_only=True)
        # Generalized date fields processing
        def get_fields(self):
            fields = super().get_fields()
            for field_name, field in fields.items():
                if isinstance(field, serializers.DateField):
                    fields[field_name] = CustomDateField(input_formats=['%Y-%m-%d'])
            return fields

        class Meta:
            model = model_class
            fields = '__all__'
    
    return ModelSerializer



# model serializers with generalized date serialization
TblRoomInfoSerializer = create_serializer(TblRoomInfo)
TblProgramSerializer = create_serializer(TblProgram)
TblDepartmentSerializer = create_serializer(TblDepartment)
TblUsersSerializer = create_serializer(TblUsers)

#basic student data
TblStudentBasicInfoSerializer = create_serializer(TblStudentBasicInfo)

#full student base data
TblStudentPersonalDataSerializer = create_serializer(TblStudentPersonalData)
TblStudentAddPersonalDataFullSerializer = create_fullstudentdata_serializer(TblStudentAddPersonalData)
TblStudentAddPersonalDataSerializer = create_serializer(TblStudentAddPersonalData)
TblStudentFamilyBackgroundSerializer = create_fullstudentdata_serializer(TblStudentFamilyBackground)
TblStudentAcademicBackgroundSerializer = create_fullstudentdata_serializer(TblStudentAcademicBackground)
TblStudentAcademicHistorySerializer = create_fullstudentdata_serializer(TblStudentAcademicHistory)


TblBugReportSerializer = create_serializer(TblBugReport)





# combined serializer for student detailed info
class StudentFullDataSerializer(serializers.Serializer):
    personal_data = TblStudentPersonalDataSerializer()
    add_personal_data = TblStudentAddPersonalDataFullSerializer()
    family_background = TblStudentFamilyBackgroundSerializer()
    academic_background = TblStudentAcademicBackgroundSerializer()
    academic_history = TblStudentAcademicHistorySerializer()

    def create(self, validated_data):
        personal_data = validated_data.pop('personal_data')
        add_personal_data= validated_data.pop('add_personal_data')
        family_background = validated_data.pop('family_background')
        academic_background = validated_data.pop('academic_background')
        academic_history = validated_data.pop('academic_history')

        personal_instance = TblStudentPersonalData.objects.create(**personal_data)

        TblStudentAddPersonalData.objects.create(fulldata_applicant_id=personal_instance, **add_personal_data)
        TblStudentFamilyBackground.objects.create(fulldata_applicant_id=personal_instance, **family_background)
        TblStudentAcademicBackground.objects.create(fulldata_applicant_id=personal_instance, **academic_background)
        TblStudentAcademicHistory.objects.create(fulldata_applicant_id=personal_instance, **academic_history)

        return {
            "personal_data": TblStudentPersonalDataSerializer(personal_instance).data,
            "add_personal_data": TblStudentAddPersonalDataFullSerializer(add_personal_data).data,
            "family_background": TblStudentFamilyBackgroundSerializer(family_background).data,
            "academic_background": TblStudentAcademicBackgroundSerializer(academic_background).data,
            "academic_history": TblStudentAcademicHistorySerializer(academic_history).data,
        }
    def validate(self, data):
        return data
