import * as actionTypes from '../constants';
const setUserInfo = (data) => {
    return {
        type: actionTypes.SET_USERINFO,
        data
    }
};
export {setUserInfo};
